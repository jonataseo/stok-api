from rest_framework.routers import DefaultRouter

from . import views

product_router = DefaultRouter()
product_router.register(r'products', views.ProductViewSet)