# coding:utf-8
"""
Vistas comunes
==============
"""

import json
from django.http import HttpResponse
from django.views.generic import View


class JSONView(View):
    """
    JSONView(View)

    Vista para el manejo de AJAX, funciona igual que
    :class:`from django.views.generic.View` con la diferencia que los métodos a
    implementar deben contener además un parámetro nombrado ``data`` y devolver
    un objeto de tipo ``list`` o ``dict`` que será directamente convertido en
    JSON para responderse. Los requests que se hagan hacia esta vista deben
    contar con el ``Content-Type`` de ``application/json``.

    Ejemplo:

    .. code:: python

        class JSONTest(JSONView):
            def get(self, request, data, *args, **kwargs):
                return {'hello': 'ajax'}

    """
    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(),
                              self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed

        data = None

        if request.method == 'POST':
            data = json.loads(request.body)
        response = handler(request, data, *args, **kwargs)
        return HttpResponse(
            content=json.dumps(response),
            content_type='application/json'
        ) if type(response) in (dict, list) else response


class JSONFormView(JSONView):
    """
    JSONFormView(JSONView)

    Vista para procesar formularios a través de AJAX mediante POST.

    :param form_class: Clase del formulario a utilizar para la validación.
    """

    form_class = None

    def post(self, request, data, *args, **kwargs):
        form = self.form_class(data=data)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return {'success': False, 'errors': form.errors}

    def form_valid(self, form):
        """
        Función que se usa para definir la respuesta de la vista cuando la
        validación del formulario es exitosa.

        :param form: La instancia del formulario validado.
        :return: La respuesta que debe recibir el cliente, por defecto es ``{'success': True}``
        :rtype: dict o list
        """
        return {'success': True}


class JSONMultiFormView(JSONView):
    """
    JSONMultiFormView(JSONView)

    Vista para procesar una lista de formularios a través de AJAX mediante POST.

    :param form_list: Lista de clases de los formularios a utilizar para la validación.
    """
    form_list = None

    def post(self, request, data, *args, **kwargs):
        form_list = [form(data=data) for form in self.form_list]
        forms_valid = False not in map(lambda f: f.is_valid(), form_list)
        errors = reduce(lambda a, b: a.update(b) or a,
                        [form.errors for form in form_list])

        if forms_valid:
            return self.form_valid(form_list, data)
        else:
            return {'success': False, 'errors': errors}

    def form_valid(self, forms, data):
        """
        Función que se usa para definir la respuesta de la vista cuando la
        validación de los formularios es exitosa.

        :param forms: Las instancias de los formularios validados.
        :param data: Los datos inicialmente enviados a la vista.
        :return: La respuesta que debe recibir el cliente, por defecto es ``{'success': True}``
        :rtype: dict o list
        """
        return {'success': True}
