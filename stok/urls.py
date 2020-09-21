from django.conf.urls import include, url
from rest_framework import urlpatterns

from client.urls import client_router
from product.urls import product_router
from sale.urls import sale_router

urlpatterns = [
    url(r'^api/', include(client_router.urls)),
    url(r'^api/', include(product_router.urls)),
    url(r'^api/', include(sale_router.urls)),
]