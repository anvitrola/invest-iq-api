from django.db import models

from account_management.models import Account

# Create your models here.

class Stock(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    ticker = models.CharField(max_length=50)
    name = models.CharField(max_length=200)

    lower_bound = models.FloatField(default=0.0)
    upper_bound = models.FloatField(default=0.0)

    close = models.FloatField(default=0.0)
    change = models.FloatField(default=0.0)
    volume = models.PositiveIntegerField(default=0)

    change_history = models.TextField(default='[]')
    
    periodicity = models.PositiveSmallIntegerField(default=1)


