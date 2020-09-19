from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Product Serializer"""

    class Meta:
        model = Product
        fields = ('id', 'name', 'quantity', 'buy_value', 'sell_value', 'date_of_last_buy')