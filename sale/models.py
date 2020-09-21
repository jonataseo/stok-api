from django.db import models
from django.db.models.deletion import SET_NULL
from client.models import Client
from product.models import Product

class Sale(models.Model):
    """Sale representation"""
    client = models.ForeignKey(Client, blank=False, null=True, on_delete=SET_NULL)
    products = models.ForeignKey(Product, related_name='products', null=True, on_delete=SET_NULL)
    date = models.DateField(blank=True, null=True)