# coding:utf-8
"""
Comunicación con el WS de SABMiller/SiteFactory
===============================================
"""

import requests
from django.conf import settings


class SABMillerService(object):
    """
    Wrapper del servicio web de SiteFactory para la consulta y registro de
    usuarios de SABMiller.

    :param api_user: Toma el valor por defecto de ``settings.SABMILLER_API_USER``.
    :param api_token: Toma el valor por defecto de ``settings.SABMILLER_API_TOKEN``.
    :param base_url: Toma el valor por defecto de ``settings.SABMILLER_SERVICE_URL``.
    """

    def __init__(self, **kwargs):
        self.api_user = kwargs.pop('api_user', settings.SABMILLER_API_USER)
        self.api_token = kwargs.pop('api_token', settings.SABMILLER_API_TOKEN)
        self.base_url = kwargs.pop('base_url', settings.SABMILLER_SERVICE_URL)

    def get_params(self, param):
        """
        Método para la obtención de parámetros de configuración para un
        formulario. **Actualmente no tiene un uso práctico.**

        :return: La estructura de la respuesta debe consultarse en la documentación del servicio web.
        :rtype: dict
        """

        response = requests.post(
            '{}/get-params'.format(self.base_url),
            {
                'api_user': self.api_user,
                'api_token': self.api_token,
                'param': param
            }
        )
        return response.json()

    def get_data(self, method, document, birthday):
        """
        Método de obtención de datos personales de un usuario.

        :param method: Método de consulta de usuarios.
        :param document: Número de documento de identidad.
        :param birthday: Fecha de nacimiento del usuario.
        :return: La estructura de la respuesta debe consultarse en la documentación del servicio web.
        :rtype: dict
        """

        response = requests.post(
            '{}/get-data'.format(self.base_url),
            {
                'metodo_select': method,
                'api_user': self.api_user,
                'api_token': self.api_token,
                'document': document,
                'field_birth_day': birthday,
            }
        )
        return response.json()

    def set_data(self, name, last_name, document, birthday, country, state,
                 city, email, phone, optin, terms, gender, twitter,
                 campaign=settings.SABMILLER_CAMPAIGN,
                 brand=settings.SABMILLER_BRAND,
                 formid=settings.SABMILLER_FORMID):
        """
        Método para registrar usuarios nuevos.

        :param name: Nombres del usuario.
        :param last_name: Apellidos del usuario.
        :param document: DNI del usuario.
        :param birthday: Fecha de nacimiento del usuario.
        :param country: País de residencia del usuario.
        :param state: Departamento de residencia del usuario.
        :param city: Provincia de residencia del usuario.
        :param email: Email del usuario.
        :param phone: Teléfono del usuario.
        :param optin: Optin del usuario.
        :param terms: Aceptación de términos/condiciones del usuario.
        :param gender: Género del usuario.
        :param twitter: Twitter handle del usuario.
        :param campaign: Campaña, por defecto utiliza ``SABMILLER_CAMPAIGN``.
        :param brand: Marca, por defecto utiliza ``SABMILLER_BRAND``.
        :param formid: FormId, por defecto utiliza ``SABMILLER_FORMID``.
        :return: La estructura de la respuesta debe consultarse en la documentación del servicio web.
        :rtype: dict
        """

        response = requests.post(
            '{}/set-data'.format(self.base_url),
            {
                'api_user': self.api_user,
                'api_token': self.api_token,
                'campaing': campaign,
                'brand': brand,
                'formid': formid,
                'name': name,
                'last-name': last_name,
                'document': document,
                'birth-day': birthday,
                'country': country,
                'state': state,
                'city': city,
                'email': email,
                'phone': phone,
                'optin': optin,
                'tyc': terms,
                'gender': gender,
                'twitter': twitter
            }
        )
        return response.json()

    def update_data(self, method, name, last_name, document, field_birthday,
                    birthday, country, state, city, email, phone, optin, terms,
                    gender, twitter, campaign=settings.SABMILLER_CAMPAIGN,
                    brand=settings.SABMILLER_BRAND,
                    formid=settings.SABMILLER_FORMID):
        """
        Método de actualización de datos de usuario.

        :param method: Método de consulta de usuario.
        :param name: Nombres del usuario.
        :param last_name: Apellidos del usuario.
        :param document: DNI del usuario.
        :param field_birthday: Fecha de nacimiento del usuario. (Requerido por el WS)
        :param birthday: Fecha de nacimiento del usuario.
        :param country: País de residencia del usuario.
        :param state: Departamento de residencia del usuario.
        :param city: Provincia de residencia del usuario.
        :param email: Email del usuario.
        :param phone: Teléfono del usuario.
        :param optin: Optin del usuario.
        :param terms: Aceptación de términos/condiciones del usuario.
        :param gender: Género del usuario.
        :param twitter: Twitter handle del usuario.
        :param campaign: Campaña, por defecto utiliza ``SABMILLER_CAMPAIGN``.
        :param brand: Marca, por defecto utiliza ``SABMILLER_BRAND``.
        :param formid: FormId, por defecto utiliza ``SABMILLER_FORMID``.
        :return: La estructura de la respuesta debe consultarse en la documentación del servicio web.
        :rtype: dict
        """

        response = requests.post(
            '{}/update-data'.format(self.base_url),
            {
                'api_user': self.api_user,
                'api_token': self.api_token,
                'metodo_update': method,
                'document': document,
                'field_birth_day': field_birthday,
                'birth-day': birthday,
                'email': email,
                'campaing': campaign,
                'brand': brand,
                'formid': formid,
                'name': name,
                'last-name': last_name,
                'country': country,
                'state': state,
                'city': city,
                'phone': phone,
                'optin': optin,
                'tyc': terms,
                'gender': gender,
                'twitter': twitter
            }
        )
        return response.json()

