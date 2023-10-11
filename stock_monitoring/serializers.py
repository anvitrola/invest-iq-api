from rest_framework import serializers

from .models import Stock


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = (
            "id",
            "created_at",
            "updated_at",
            "ticker",
            "name",
            "lower_bound",
            "upper_bound",
            "close",
            "change",
            "volume",
            "periodicity",
        )
