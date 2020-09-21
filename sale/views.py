from rest_framework import viewsets

from .models import Sale
from .serializers import SaleSerializer


class SaleViewSet(viewsets.ModelViewSet):
    """EndPoint for list and create sales."""

    queryset = Sale.objects.order_by('date')
    serializer_class = SaleSerializer