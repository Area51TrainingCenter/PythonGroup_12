# coding:utf-8
"""
Vistas de validación y registro de usuarios
===========================================
"""

from datetime import datetime

from common.sabmiller.forms import SABMillerUserValidationForm, \
    SABMillerUserRegistrationForm
from common.sabmiller.service import SABMillerService
from common.views import JSONFormView


class SABMillerUserValidation(JSONFormView):
    """
    SABMillerUserValidation(JSONFormView)

    Vista de validación de usuarios de SABMiller. Tiene una URL definida como
    ``/validate`` en :mod:`common.sabmiller.urls` y recibe mediante POST un
    JSON con los datos del formulario definido en
    :class:`common.sabmiller.forms.SABMillerUserValidationForm`

    :return: JSON con el formato ``{"success": true, "data": {}, "errors", null}``
    :rtype: JSON
    """

    form_class = SABMillerUserValidationForm

    def form_valid(self, form):
        response = SABMillerService().get_data(
            method='metodo-3',
            document=form.cleaned_data['document'],
            birthday=form.cleaned_data['birthday']
        )

        if 'code' in response.get('response', {}):
            code = response['response']['code']
            print code
            if code in (214, 215):
                return {'success': True, 'data': {}}
            elif code == 217:
                return {'success': False,
                        'errors': {'birthday': [u'La fecha de nacimiento no '
                                                u'coincide con el registro.']}}
            else:
                return {'success': False,
                        'errors': {'document': [u'Datos de entrada inválidos.']}}
        elif 'data_form' in response.get('response', {}):
            data = response['response']['data_form']
            if datetime.strptime(data['birth_day'], '%d/%m/%Y').date() \
            != form.cleaned_data['birthday']:
                return {'success': False,
                        'errors': {'birthday': [u'La fecha de nacimiento no '
                                                u'coincide con el registro.']}}
            return {
                'success': True,
                'data': data
            }

        return response


class SABMillerUserRegister(JSONFormView):
    """
    SABMillerUserRegister(JSONFormView)

    Vista de registro de usuarios de SABMiller. Tiene una URL definida como
    ``/register`` en :mod:`common.sabmiller.urls` y recibe mediante POST un
    JSON con los datos del formulario definido en
    :class:`common.sabmiller.forms.SABMillerUserRegistrationForm`

    :return: JSON con el formato ``{"success": true, "result": {}}``
    :rtype: JSON
    """

    form_class = SABMillerUserRegistrationForm

    def form_valid(self, form):
        data = form.cleaned_data
        document = data['document']
        birthday = data['birthday']
        service = SABMillerService()
        response = service.get_data(method='metodo-3', document=document,
                                    birthday=birthday)

        data['birthday'] = data['birthday'].strftime('%d/%m/%Y')
        data['country'] = u'Perú'

        if 'data_form' in response.get('response', {}):
            data['field_birthday'] = birthday
            data['method'] = 'metodo-3'
            method = service.update_data
        else:
            method = service.set_data

        response = method(**data)
        if 'result' in response:
            return {'success': False, 'result': response['result']}
        else:
            return {'success': True}
