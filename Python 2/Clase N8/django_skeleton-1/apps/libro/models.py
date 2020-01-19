from django.db import models
from lectores.models import Lector

class Libro_Consultado(models.Model):
    name = models.CharField(verbose_name='Titulo', max_length=200)
    author = models.CharField(verbose_name='Autor', max_length=200)
    year = models.DateField(verbose_name='Año de publicacion')
    lector = models.ForeignKey(Lector, on_delete=models.SET_NULL, null=True)


