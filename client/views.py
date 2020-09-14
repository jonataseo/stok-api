from rest_framework import viewsets

from .models import Client
from .serializers import ClientSerializer


class DefaultMinix(object):
    """Pagination config"""
    paginate_by = 1
    paginate_by_param = 'page_size'
    max_paginate_by = 100

class ClientViewSet(viewsets.ModelViewSet):
    """Endpoints for list and create clients"""

    queryset = Client.objects.order_by('name')
    serializer_class = ClientSerializer