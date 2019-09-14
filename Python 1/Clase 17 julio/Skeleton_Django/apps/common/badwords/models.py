# coding:utf-8
from django.db import models


class BadWord(models.Model):
    """
    BadWord()

    Modelo simple que representa a una palabra a filtrar.

    :param word: Palabra a filtrar.
    :type word: CharField
    """

    word = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )
