# coding:utf-8
"""
Utilidades de Facebook
======================
"""

from django.shortcuts import redirect
from django.views.generic.base import ContextMixin
from django.conf import settings

from open_facebook.api import FacebookAuthorization, OpenFacebook


def get_signed_request(request):
    """
    Función utilitaria que descifra y recoge el request firmado que Facebook
    entrega en algunos escenarios.

    .. note::

        Requiere la instalación del módulo` ``django_facebook``.

    :param request: Una instancia de ``django.request``.
    :return: TODO
    """

    try:
        if request.session.get('signed_request', None) \
                and request.method.upper() != 'POST':
            sgr = request.session['signed_request']
        else:
            if not 'signed_request' in request.POST:
                sgr = request.session['signed_request']
            else:
                sgr = request.POST.get('signed_request')
                request.session['signed_request'] = sgr
        result = FacebookAuthorization.parse_signed_data(sgr)
        # }
        return result
    except Exception as e:
        # print e
        return None


class FacebookContextMixin(ContextMixin):
    """
    Mixin de datos de Facebook.

    Un mixin de contexto para todos los TemplateViews y derivados que deseen
    incluir algunas variables de los settings en el contexto. Este mixin puede
    ser (y debería) sustituido por el common context processor del módulo
    ``context-processors``.

    Las variables que se incluyen en el contexto al usar este mixin son:
        - ``base_url`` tiene el valor de ``ROOT_URL``
        - ``app_id`` tiene el valor de ``FACEBOOK_APP_ID``
        - ``scope`` tienee el valor de ``FACEBOOK_SCOPE``
    """

    def get_context_data(self, **kwargs):
        context = super(FacebookContextMixin, self).get_context_data(**kwargs)
        context.update({
            'base_url': settings.ROOT_URL,
            'app_id': settings.FACEBOOK_APP_ID,
            'scope': settings.FACEBOOK_SCOPE,
        })
        return context


class FacebookProtectionMixin(object):
    """
    Mixin de protección de Views para Facebook.

    Este mixin revisa la existencia de una sesión activa en Facebook en la
    vista comprobando la existencia de un signed request. Útil para cuando se
    tenga una vista que sólo debe de ser visitada desde un canvas de Facebook.
    """

    def dispatch(self, request, *args, **kwargs):
        self.signed = get_signed_request(request)
        if not self.signed:
            return redirect('https://apps.facebook.com/%s' %
                            settings.FACEBOOK_APP_ID)
        return super(FacebookProtectionMixin, self).\
            dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)
