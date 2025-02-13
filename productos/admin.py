from django.contrib import admin
from .models import Producto

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria', 'imagen')
    list_filter = ('categoria',)
    search_fields = ('nombre',)

admin.site.register(Producto, ProductoAdmin)