# coding:utf-8
"""
Decoradores
===========
"""


def p3p_policy(view_function):
    """
    Decorador de views para agregar cabeceras de P3P. Especialmente útil cuando
    se tiene funcionalidad que se comporta de manera anómala bajo Internet
    Explorer en caso se tenga  el sitio embebido en un `iframe`.

    Para usarlo, sólo hace falta agregarlo como un decorador de la vista:

    .. code:: python

        # urls.py
        url(r'^$', p3p_policy(views.Home.as_view()), name='home')
    """

    def wrapper(request, *args, **kwargs):
        response = view_function(request, *args, **kwargs)
        response['P3P'] = 'policyref="/w3c/p3p.xml", CP="IDC DSP COR IVAi ' \
                          'IVDi OUR TST"'
        return response
    return wrapper
