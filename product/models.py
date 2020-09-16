from django.db import models
from django.utils.translation import ugettext_lazy as _ 


class Product(models.Model):
    """Product Representation"""
    name = models.CharField(max_length=100, blank=False)
    quantity = models.PositiveIntegerField(blank=False, default=0)
    buy_value = models.DecimalField(blank=False, decimal_places=2, max_digits=8)
    sell_value = models.DecimalField(blank=False, decimal_places=2, max_digits=8)


    def profit(self):
        return self.sell_value - self.buy_value