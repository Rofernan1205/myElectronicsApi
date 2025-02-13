from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, ProductoListAPIView

productoRouter = DefaultRouter()
productoRouter.register(prefix='productos', basename='productos', viewset=ProductoViewSet)

urlpatterns = [
    path('productos/categoria/', ProductoListAPIView.as_view(), name='productos_categoria'),
    path('', include(productoRouter.urls)),
]