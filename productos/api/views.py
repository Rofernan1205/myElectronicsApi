from rest_framework import generics
from ..models import Producto
from django_filters.rest_framework import  DjangoFilterBackend
from .serializers import ProductoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

class ProductoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre', 'categoria']