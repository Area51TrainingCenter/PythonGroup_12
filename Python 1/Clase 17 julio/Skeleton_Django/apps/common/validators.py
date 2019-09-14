# coding:utf-8
"""
Validadores de entrada
======================
"""

from django.core.validators import RegexValidator

name_validator = RegexValidator(ur'^[a-zA-z \-\'áéíóúÁÉÍÓÚñÑüÜïÏöÖ]+$')
"""
Valida la presencia de caracteres alfabéticos y especiales adecuados para un
nombre.
"""

dni_validator = RegexValidator(ur'^[0-9]{8}$')
"""Valida la presencia de 8 caracteres numéricos."""

phone_validator = RegexValidator(ur'^\+?[0-9 -]{7,14}$')
"""
Valida la presencia de 7 a 14 caracteres numéricos con espacios y guiones
(``-``).
"""

alphanumeric_validator = RegexValidator(ur'^[ -~áéíóúÁÉÍÓÚñÑüÜ¡¿]+$')
"""
Valida la presencia de todos los caracteres imprimibles incluyendo aquellos
usados en el idioma castellano.
"""
