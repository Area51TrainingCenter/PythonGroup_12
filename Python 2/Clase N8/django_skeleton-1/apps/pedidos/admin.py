from django.contrib import admin
from .models import Pedidos


class Pedidos_Admin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad', 'cliente', 'producto', 'precio')


admin.site.register(Pedidos, Pedidos_Admin)