# coding:utf-8
from django.db import models


class Ubigeo(models.Model):
    """
    Ubigeo()

    Modelo que representa una división geográfica peruana.

    :param name: Nombre de la división.
    :type name: CharField

    :param parent: División de orden superior.
    :type parent: ForeignKey(Ubigeo)
    """

    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', blank=True, null=True)

