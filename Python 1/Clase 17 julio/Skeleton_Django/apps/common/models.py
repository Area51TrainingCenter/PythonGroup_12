# coding:utf-8
"""
Utilidades para Modelos
=======================
"""

import os
import uuid

from django.utils.deconstruct import deconstructible


@deconstructible
class file_rename(object):
    """
    Esta clase puede usarse en la definición de un FileField (o similares)
    para renombrar los archivos subidos con un uuid4 y un prefijo opcional.

    Para usarlo, sólo usa la función en el argumento ``upload_to`` de tu
    FileField:

    .. code:: python

        # models.py
        image = models.FileField(
            upload_to=file_rename('images')
        )

    """
    def __init__(self, folder='', prefix=None):
        self.folder = folder
        self.prefix = prefix

    def __call__(self, instance, filename):
        extension = filename.split('.')[-1] \
            if len(filename.split('.')) > 1 else 'unknown'

        final_filename = u'{}{}.{}'.format(
            self.prefix + '_' if self.prefix else '',
            uuid.uuid4().get_hex()[:10],
            extension
        )

        return os.path.join(self.folder, final_filename)


class FakeCharField():
    """
    Clase que finge ser un CharField sin tener efecto en la base de datos. Se
    puede utilizar para tareas que requieran simular la existencia de un campo
    temporal sin afectar el modelo de datos original.
    """

    def __new__(cls, value=None, short_description=None):
        self = super(FakeCharField, cls).__new__(cls, value)
        self.short_description = short_description
        return self

