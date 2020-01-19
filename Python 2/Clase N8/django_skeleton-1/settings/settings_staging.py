# coding:utf-8
from settings import *

SECRET_KEY = 'bmbng=u=@z@l78k#lh2xp!anqu#4v_)gm1of8n29077$c^5=%u'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wxbaskyc',
        'USER': 'wxbaskyc',
        'PASSWORD': 'CD9rvPJMU_tNsEyhSfJF_O_Xjw_n62yF',
        'HOST': 'salt.db.elephantsql.com',
        'PORT': '',
    },
}

DEBUG = True
BASE_URL = 'http://localhost:8000'
