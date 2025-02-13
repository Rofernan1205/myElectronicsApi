from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=255, unique=True, verbose_name="Nombre")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")

    def __str__(self):
        return f" {self.nombre}"

    class Meta:
        verbose_name = "Categoria"  # Nombre en singular
        verbose_name_plural = "Categorías"  # Nombre en plural
