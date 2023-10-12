import json
import logging
import os
import requests
from django.utils import timezone
from django.core.mail import send_mail
from celery import shared_task

from stock_monitoring.models import Stock

logger = logging.getLogger(__name__)


@shared_task
def monitor_stocks():
    logger.info("Task started.")

    stocks = Stock.objects.values_list("ticker", flat=True).distinct()
    token = os.getenv("BRAPI_API_TOKEN")

    ticker_urls = [
        f"https://brapi.dev/api/quote/{ticker}?token={token}" for ticker in stocks
    ]

    responses = [requests.get(url) for url in ticker_urls]
    current_time = timezone.now()

    for res in responses:
        if res.status_code == 200:
            logger.info("Performed requests.")

            data = res.json()
            result = data["results"][0]

            current_change = result["regularMarketChange"]
            current_close = result["regularMarketPrice"]

            stocks = Stock.objects.filter(ticker=result["symbol"])

            for stock in stocks:
                periodicity = stock.periodicity

                time_difference_minutes = (
                    current_time - stock.updated_at
                ).total_seconds() / 60

                # We check if stock was just updated - respecting the periodicity our client choose
                # And we check if the stock price has changed. If it's the same we don't do anything
                if (
                    time_difference_minutes > periodicity
                    and stock.close != current_close
                ):
                    # Saving the stock close and change values before updating them
                    old_close = stock.close
                    old_change = stock.change

                    # We update the stock price since it has changed
                    stock.close = current_close
                    stock.change = current_change

                    change_history = json.loads(stock.change_history)

                    change_history.append(
                        {
                            "change": old_change,
                            "date": stock.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
                            "close": old_close,
                        }
                    )

                    stock.change_history = json.dumps(change_history)
                    stock.updated_at = current_time

                    stock.save()

                    # If stock price went down and if the current price is <= than the lower bound
                    if current_change < 0 and current_close <= stock.lower_bound:
                        print(f"\tIt's time to buy {result['symbol']}! Hurry up!")
                        send_mail(
                            f"It's time to buy {result['symbol']}.",
                            f"\tThis stock price has changed! It was R${old_close} but now it is R${current_close}, change of {current_change}. It has reached your lower bound value of R${stock.lower_bound}, indicating it is a good time to buy this stock. Good luck!",
                            None,
                            [stock.account.email],
                            fail_silently=False,
                        )

                    # If stock price went up and if the current price is >= than the upper bound
                    if current_change > 0 and current_close >= stock.upper_bound:
                        print(f"\tIt's time to sell {result['symbol']}! Hurry up!")

                        send_mail(
                            f"It's time to sell {result['symbol']}.",
                            f"\tThis stock price has changed! It was R${old_close} but its last change price is R${current_close}, change of {current_change}. It has reached your upper bound value of R${stock.upper_bound}, indicating it is a good time to sell this stock. Good luck!",
                            None,
                            [stock.account.email],
                            fail_silently=False,
                        )
                else:
                    continue
