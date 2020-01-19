from django.contrib import admin
from .models import Productos


class Productos_Admin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')


admin.site.register(Productos, Productos_Admin)
