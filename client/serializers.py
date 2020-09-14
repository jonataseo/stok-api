from rest_framework import serializers

from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    """Client Serializer"""

    class Meta:
        model = Client
        fields = ('id', 'name', 'phone', 'street_name', 'number', 'compliment', 
            'neighborhood', 'zipcode')