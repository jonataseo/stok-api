from rest_framework.routers import DefaultRouter

from . import views

client_router = DefaultRouter()
client_router.register(r'clients', views.ClientViewSet)