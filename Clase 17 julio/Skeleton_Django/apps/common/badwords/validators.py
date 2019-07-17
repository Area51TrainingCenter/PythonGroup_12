# coding:utf-8
import re

from django.db.models import Q

from common.badwords.models import BadWord


def is_bad_word(text):
    """
    Función para determinar la validez de un texto contra la lista de palabras
    existentes en la base de datos.

    :param text: La cadena que se validará.
    :type text: str o unicode
    :return: Un booleano representando la validez del texto.
    :rtype: bool
    """

    text = text.strip()
    text = re.sub(r'\s+', u' ', text)
    rules = [
        (r'1', u'i'),
        (r'2', u'dos'),
        (r'3', u'e'),
        (r'4', u'a'),
        (r'5', u's'),
        (r'6', u'g'),
        (r'7', u't'),
        (r'8', u'b'),
        (r'9', u'g'),
        (r'0', u'o'),
        (r'[^\w\s]+', u'')
    ]

    validation_text = text[:]

    for pattern, replace in rules:
        validation_text = re.sub(pattern, replace, validation_text,
                                 flags=re.UNICODE)

    initial_validation = Q(word__iexact=validation_text)
    validation_text = validation_text.split(' ')
    validation_text = [Q(word__iexact=t) for t in validation_text]
    validation_text.append(initial_validation)
    query = reduce(lambda x, y: x | y, validation_text)
    return BadWord.objects.filter(query).exists()
