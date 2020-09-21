from rest_framework.routers import DefaultRouter

from . import views

sale_router = DefaultRouter()
sale_router.register(r'sales', views.SaleViewSet)