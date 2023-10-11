import json

from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED,
    HTTP_200_OK
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


from stock_monitoring.models import Stock
from stock_monitoring.serializers import StockSerializer


class CreateStockMonitor(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = request.data
        account = request.user

        try:
            stock = {
                "name": data.get("name"),
                "ticker": data.get("ticker"),
                "lower_bound": data.get("lower_bound"),
                "upper_bound": data.get("upper_bound"),
                "periodicity": data.get("periodicity"),
                "close": data.get("close"),
                "change": data.get("change"),
                "volume": data.get("volume"),
            }

            stock_obj = Stock.objects.filter(
                account=account, ticker=data.get("ticker")
            ).first()

            if stock_obj:
                for key, value in stock.items():
                    setattr(stock_obj, key, value)

                # Save the updated stock object
                stock_obj.save()
            else:
                Stock.objects.create(account=account, **stock)

        except Exception as e:
            return Response({"error": str(e)}, status=HTTP_400_BAD_REQUEST)

        return Response(
            {"message": "Stock successfully added to monitoring"},
            status=HTTP_201_CREATED,
        )


class GetMonitoredStocksList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        account = request.user

        try:
            stock_obj = Stock.objects.filter(account=account)

        except Exception as e:
            return Response({"error": str(e)}, status=HTTP_400_BAD_REQUEST)

        return Response(
            StockSerializer(stock_obj, many=True).data, status=HTTP_201_CREATED
        )


class GetMonitoredStocksChangesHistory(APIView):
    permission_classes = (IsAuthenticated,)
    # pagination_class = PageNumberPagination  # Use PageNumberPagination or another pagination class of your choice
    # page_size = 5  # Set the number of items per page as needed

    def get(self, request, *args, **kwargs):
        account = request.user
        ticker = request.GET.get("ticker", "")

        try:
            history_queryset = Stock.objects.filter(
                account=account, ticker=ticker
            ).values_list("change_history", flat=True)

            if history_queryset.exists():
                history_array = json.loads(history_queryset[0])
                print('HISTORY')
                print(history_array)

                # page = self.paginate_queryset(history_array)

                # if page is not None:
                #     return self.get_paginated_response(page)

        except Exception as e:
            return Response({"error": str(e)}, status=HTTP_400_BAD_REQUEST)

        return Response(history_array, status=HTTP_200_OK)
        

class GetMonitoredStocksDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        account = request.user
        ticker = request.GET.get("ticker", "")

        try:
           stock = Stock.objects.filter(account=account, ticker=ticker).first()
           
        except Exception as e:
            return Response({"error": str(e)}, status=HTTP_400_BAD_REQUEST)

        return Response(StockSerializer(stock).data, status=HTTP_200_OK)
        
