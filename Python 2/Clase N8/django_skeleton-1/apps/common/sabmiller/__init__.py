# coding:utf-8
"""
Utilidades y funciones de SABMiller
===================================

Un conjunto de clases, vistas y funciones útiles para interactuar con los
servicios de SABMiller/SiteFactory.

Para instalarlo, añadirlo en ``INSTALLED_APPS``:

    .. code:: python

        INSTALLED_APPS = (
            # ...
            'common.sabmiller',
            # ...
        )

Se deben definir las siguientes constantes en el archivo de configuración (los
valores de estas son suministrados por SiteFactory):

    - ``SABMILLER_API_USER``
    - ``SABMILLER_API_TOKEN``
    - ``SABMILLER_SERVICE_URL``
    - ``SABMILLER_CAMPAIGN``
    - ``SABMILLER_BRAND``
    - ``SABMILLER_FORMID``

Esta aplicación incluye dos vistas para realizar la validación y registro de
usuarios, sus urls se pueden agregar al archivo ``urls.py`` general:

    .. code:: python

        urlpatterns = [
            # ...
            url(r'^sabmiller/', include('common.sabmiller.urls')),
            # ...
        ]


.. automodule:: common.sabmiller.forms
   :members:


.. automodule:: common.sabmiller.service
   :members:


.. automodule:: common.sabmiller.views
   :members:

"""
