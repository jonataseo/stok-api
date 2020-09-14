from django.conf.urls import include, url
from rest_framework import urlpatterns

from client.urls import router

urlpatterns = [
    url(r'^api/', include(router.urls)),
]