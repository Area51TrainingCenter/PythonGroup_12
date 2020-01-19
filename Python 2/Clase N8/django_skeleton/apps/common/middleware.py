# coding:utf-8
"""
Middewares comunes
==================
"""

import re

from django.http import HttpResponseRedirect


class IEDetectionMiddleware(object):
    """
    Middleware para detectar versiones anteriores de Internet Explorer y
    redireccionar al usuario hacia browsehappy.com.
    """
    def process_request(self, request):
        pass

