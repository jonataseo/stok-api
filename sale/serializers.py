from django.db.models import fields
from rest_framework import serializers
from product.models import Product
from product.serializers import ProductSerializer

from .models import Sale

class SaleSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Sale
        fields = ('id', 'client', 'products', 'date')