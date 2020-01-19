from django.db import models


class Clientes(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    numero = models.CharField(max_length=15)
