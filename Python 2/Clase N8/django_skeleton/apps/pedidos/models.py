from django.db import models
from clientes.models import Clientes
from productos.models import Productos


class Pedidos(models.Model):
    nombre = models.CharField(max_length=20, verbose_name=u'Nombre')
    cantidad = models.PositiveIntegerField(verbose_name=u'Cantidad')
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, verbose_name=u'Cliente')
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE, verbose_name=u'Producto')
    precio = models.DecimalField(max_digits=10, decimal_places=10, verbose_name=u'Precio', default=0)

    def __str__(self):
        return str(self.nombre)
