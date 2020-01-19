from django.contrib import admin
from .models import Clientes


class Clientes_Admin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'numero')


admin.site.register(Clientes, Clientes_Admin)