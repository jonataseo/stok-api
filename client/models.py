from django.db import models
from django.utils.translation import ugettext_lazy as _

from phone_field import PhoneField

class Client(models.Model):
    """Client representation"""
    name = models.CharField(max_length=100, blank=False)
    phone = PhoneField(max_length=31, blank=False)
    #Endereço
    street_name = models.CharField(max_length=120, blank=False)
    number = models.SmallIntegerField(blank=True, default=0)
    compliment = models.CharField(max_length=100, blank=True)
    neighborhood = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=15, blank=True)