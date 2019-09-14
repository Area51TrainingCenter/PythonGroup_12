# coding:utf-8
"""
Vistas de consulta de Ubigeos
=============================
"""

from common.ubigeo.models import Ubigeo
from common.views import JSONView


class UbigeoView(JSONView):
    """
    UbigeoView(JSONView)

    Vista para consultar la lista de ubigeos en función a un nivel superior
    dado. Tiene una URL definida como ``/`` en :mod:`common.ubigeo.urls` y
    recibe mediante GET el id del Ubigeo a usar como filtro de orden superior
    (parámetro de nombre ``parent``). Si no se suministra, se obtendrán todos
    los ubigeos de primer orden (Departamentos).

    :return: JSON con el formato ``[{"id": 1, "name": ""}, ...]``
    :rtype: JSON
    """

    def get(self, request, data, *args, **kwargs):
        return [
            {'id': ubigeo.id, 'name': ubigeo.name}
            for ubigeo
            in Ubigeo.objects.filter(parent__id=request.GET.get('parent') or None)
        ]
