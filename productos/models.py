from django.db import models
from categorias.models import Categoria
import cloudinary
from cloudinary.models import CloudinaryField


# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    nombre_comercial = models.CharField(max_length=200, blank=True, null=True, verbose_name="Nombre comercial")
    descripcion = models.CharField(max_length=300, blank=True, null=True, verbose_name='Descripción')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    modelo = models.CharField(max_length=80, verbose_name='Modelo')
    marca = models.CharField(max_length=100, verbose_name="Marca")
    procesador= models.CharField(max_length=100, null=True, blank=True, verbose_name="Procesador")
    Tamano_pantalla = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True, verbose_name="Tamaño de pantalla")
    altura = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True, verbose_name="Altura")
    Largo = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True, verbose_name="Largo")
    pais_origen = models.CharField(max_length=60, verbose_name="Pais de origen")
    accesorios = models.CharField(max_length=400, verbose_name="Accesorios")
    imagen = CloudinaryField('images', blank=True)
    img = CloudinaryField('imgs', blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="productos")

    def __str__(self):
        return f"{self.nombre} ({self.modelo})"

    class Meta:
        verbose_name = "Producto"  # Nombre en singular
        verbose_name_plural = "Productos"  # Nombre en plural
