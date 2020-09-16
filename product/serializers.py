from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Product Serializer"""

    class Meta:
        model = Product
        fields = ('id', 'name', 'quantity', 'buy_price', 'sell_price')