# coding:utf-8
"""
Envío de SMS
============
"""

from pysimplesoap.client import SoapClient
from django.conf import settings


class SMS:
    """
    Clase utilitaria para envío de SMS a través de la plataforma de Tedexis,
    que tiene un servicio SOAP para este propósito.

    Requiere la presencia de las siguientes constantes en los settings:
        - ``SOAP_URI`` la URL al servicio de envío
        - ``SOAP_TEXT`` el texto por defecto a enviar cuando se use ``send()``
        - ``SOAP_PASSPORT`` `pasaporte` de identificación suministrado por Tedexis.
        - ``SOAP_PASSWORD`` contraseña del servicio suministrada por Tedexis.

    Uso:

    .. code:: python

        sms = SMS()
        sms.send('987654321', 'hola!')

    """

    def __init__(self):
        self.sms_uri = settings.SOAP_URI

    def send(self, number, text=None):

        # Fallback for text
        text = text or settings.SOAP_TEXT

        # defining sms wsdl uri
        client = SoapClient(wsdl=self.sms_uri, trace=False)

        # preparing request
        number = "51" + number
        response = client.sendSMS(
            passport=settings.SOAP_PASSPORT,
            password=settings.SOAP_PASSWORD,
            text=text,
            number=number
        )

        if response['return'] == 0:
            return True
        else:
            return False
