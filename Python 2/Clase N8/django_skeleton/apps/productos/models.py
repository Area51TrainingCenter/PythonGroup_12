from django.db import models
from clientes.models import Clientes


class Productos(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=10, decimal_places=10, verbose_name=u'Precio')

    def __str__(self):
        return str(self.nombre)