from django.contrib import admin
from .models import Libro_Consultado


class Libro_Admin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Libro_Consultado, Libro_Admin)
