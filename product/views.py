from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer

class DefaultMinix(object):
    """Pagination config"""
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100

class ProductViewSet(viewsets.ModelViewSet):
    """Endpoint for list, create, delete and update products"""

    queryset = Product.objects.order_by('name')
    serializer_class = ProductSerializer