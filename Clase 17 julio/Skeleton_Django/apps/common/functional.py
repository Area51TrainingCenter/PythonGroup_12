# coding:utf-8
"""
Utilidades de naturaleza funcional
==================================
"""


def property_lazy(fn):
    """
    Utilidad de decoración de propiedades de clase como perezosas.

    Ejemplo:

    .. code:: python

        from common.functional import property_lazy

        class Test:
            @property_lazy
            def value(self):
                return something

    :param fn: Función a decorar.
    :type fn: function
    :return: Función decorada como perezosa.
    """
    attr_name = '_lazy_' + fn.__name__

    @property
    def _lazyprop(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)
    return _lazyprop
