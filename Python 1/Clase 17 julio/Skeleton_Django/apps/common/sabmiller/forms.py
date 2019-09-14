# coding:utf-8
"""
Formularios de validación y registro de usuarios
================================================
"""

import datetime

from django import forms

from common.validators import dni_validator, alphanumeric_validator, \
    phone_validator
from dateutil import relativedelta


class SABMillerUserValidationForm(forms.Form):
    """
    SABMillerUserValidationForm()

    Formulario de validación de usurarios de SABMiller.

    :param document: DNI con máximo de 8 caracteres.
    :type document: CharField

    :param birthday: Fecha de nacimiento en formato YYY-MM-DD.
    :type birthday: DateField
    """

    document = forms.CharField(max_length=8, strip=True,
                               validators=[dni_validator], required=True)
    birthday = forms.DateField(input_formats=['%Y-%m-%d'], required=True,
                               localize=False)

    def clean_birthday(self):
        """
        Función de validación de la fecha de nacimiento. Lanza una excepción
        del tipo ``ValidationError`` cuando la fecha tiene una distancia menor
        a 18 años respecto a la actual.
        """

        birth_date = self.cleaned_data.get('birthday')
        if birth_date:
            age = relativedelta.relativedelta(
                datetime.datetime.now().date(),
                birth_date
            )

            if age.years < 18:
                raise forms.ValidationError(
                    u'Debes ser mayor de edad para poder participar.'
                )

        return birth_date


class SABMillerUserRegistrationForm(forms.Form):
    """
    SABMillerUserRegistrationForm()

    Formulario de registro de usurarios de SABMiller.

    :param name: Nombres del usuario. Máximo 35 caracteres. Obligatorio.
    :type name: CharField

    :param last_name: Apellidos del usuario. Máximo 80 caracteres. Obligatorio.
    :type last_name: CharField

    :param document: DNI del usuario. Máximo 8 caracteres. Obligatorio.
    :type document: CharField

    :param birthday: Fecha de nacimiento del usuario. Formato YYYY-MM-DD. Obligatorio.
    :type birthday: DateField

    :param gender: Género del usuario. Opciones: 'Masculino' o 'Femenino'. Obligatorio.
    :type gender: CharField

    :param state: Departamento del usuario. Máximo 50 caracteres. Obligatorio.
    :type state: CharField

    :param city: Provincia del usuario. Máximo 50 caracteres. Obligatorio.
    :type city: CharField

    :param email: Email del usuario. Obligatorio.
    :type email: EmailField

    :param phone: Teléfomo del usuario. Máximo 9 caracteres. Opcional.
    :type phone: CharField

    :param twitter: Handle de Twitter del usuario. Máximo 255 caracteres. Opcional.
    :type twitter: CharField

    :param optin: Optin del usuario. Opciones: 1 o 0. Obligatorio.
    :type optin: IntegerField

    :param terms: Aceptación de términos. Opciones: 1 o 0. Obligatorio.
    :type terms: IntegerField
    """

    name = forms.CharField(
        max_length=35,
        validators=[alphanumeric_validator],
        strip=True,
        required=True,
    )

    last_name = forms.CharField(
        max_length=80,
        validators=[alphanumeric_validator],
        strip=True,
        required=True,
    )

    document = forms.CharField(
        max_length=8,
        validators=[dni_validator],
        strip=True,
        required=True,
    )

    birthday = forms.DateField(
        input_formats=['%Y-%m-%d'],
        localize=False,
        required=True,
    )

    gender = forms.ChoiceField(
        choices=((u'Masculino', u'Masculino'),
                 (u'Femenino', u'Femenino')),
        required=True,
    )

    # country = u'Perú'

    # Department
    state = forms.CharField(
        max_length=50,
        strip=True,
        required=True,
    )

    # Province
    city = forms.CharField(
        max_length=50,
        strip=True,
        required=True,
    )

    email = forms.EmailField(required=True)

    phone = forms.CharField(
        max_length=9,
        validators=[phone_validator],
        initial='',
        required=False,
    )

    twitter = forms.CharField(
        max_length=255,
        initial='',
        required=False,
    )

    optin = forms.IntegerField(
        max_value=1,
        min_value=0,
        initial=0,
        required=True
    )

    terms = forms.IntegerField(
        max_value=1,
        min_value=0,
        required=True
    )
