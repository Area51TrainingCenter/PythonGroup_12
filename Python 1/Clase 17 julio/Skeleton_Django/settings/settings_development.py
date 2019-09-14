# coding:utf-8
from settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True
BASE_URL = 'http://localhost:8000'
# ROOT_URLCONF = 'settings.urls'
