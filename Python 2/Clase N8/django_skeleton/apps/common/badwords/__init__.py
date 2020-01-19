# coding:utf-8
"""
Validador de palabras restringidas
==================================

Este módulo permite incluir una lista de palabras restringidas persistente en
base de datos e incluye una función para validar cualquier cadena de texto
contra esta lista.

Para instalarlo, añadirlo en ``INSTALLED_APPS``:

    .. code:: python

        INSTALLED_APPS = (
            # ...
            'common.badwords',
            # ...
        )

Y efectuar un ``migrate``:

    ::

        python settings/manage.py migrate badwords

.. note::
    Este módulo no cuenta con datos iniciales y por tanto deben ser
    insertados manualmente en la tabla ``badwords_badword``.

.. automodule:: common.badwords.models
   :members:

.. automodule:: common.badwords.validators
   :members:
"""
