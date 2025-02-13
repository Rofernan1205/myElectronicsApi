from .views import CategoriaViewSet
from rest_framework.routers import DefaultRouter

categoriaRouter = DefaultRouter()
categoriaRouter.register(prefix='categorias', basename='categorias', viewset=CategoriaViewSet)
urlpatterns = categoriaRouter.urls