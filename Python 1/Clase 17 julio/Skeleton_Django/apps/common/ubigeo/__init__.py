# coding:utf-8
"""
Ubigeo
======

Modelos y vistas útiles para manejar las divisiones políticas del Perú.

Para instalarlo, añadirlo en ``INSTALLED_APPS``:

    .. code:: python

        INSTALLED_APPS = (
            # ...
            'common.ubigeo',
            # ...
        )

Y efectuar un ``migrate``. Esto cargará en la tabla ``ubigeo_ubigeo`` una lista
completa de ubigeos:

    ::

        python settings/manage.py migrate ubigeo

Esta aplicación incluye una vista de consulta de ubigeos, cuya url se puede
agregar al archivo ``urls.py`` general:

    .. code:: python

        urlpatterns = [
            # ...
            url(r'^ubigeo/', include('common.ubigeo.urls')),
            # ...
        ]


.. automodule:: common.ubigeo.models
   :members:


.. automodule:: common.ubigeo.views
   :members:

"""
