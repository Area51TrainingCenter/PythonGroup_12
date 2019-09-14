# coding:utf-8
"""
Procesadores de contexto
========================
"""

from django.conf import settings


def common(request):
    """
    Context processor común. Agrega un número de constantes de los settings de
    django al contexto de todas las plantillas a renderizarse.

    Actualmente añade las siguientes contantes:
        - ``BASE_URL``
        - ``FACEBOOK_ID``
        - ``CAMPAIGN_ID``

    No debe utilizarse directamente, sino agregarse a la variable
    ``context_processors`` como parte de la constante ``TEMPLATES`` del settings.
    """

    settings_to_include = [
        'BASE_URL',
        'FACEBOOK_ID',
        'CAMPAIGN_ID'
    ]

    return {
        name: getattr(settings, name)
        for name in settings_to_include if hasattr(settings, name)
    }
