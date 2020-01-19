# coding:utf-8

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

CELERY_BROKER_URL = 'amgp://localhost'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bmbng=u=@z@l78k#lh2xp!anqu#4v_)gm1of8n29077$c^5=%u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.contenttypes',

    # 'grappelli.dashboard',
    'grappelli',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'channels'
    # Common modules
    #'common',
    # 'common.sabmiller',
    # 'common.ubigeo',
    # 'common.badwords',

    # Optional utilities:
    'corsheaders',

    # Your apps here:
    'clientes',
    'productos',
    'pedidos',
    'lectores',
    'libro',
    'blog',
    'rest_framework',

    # ...
    #'website',
)

CHANNEL_LAYER = {
    'default': {
        'BACKEND': 'channels_redis.RedisChannelLayer',
        ''
        'CONFIG': {
            'host': [('localhost', 6379)],
        },
        'ROUTING': 'chantest.routing.channel_routing',
    }
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'website.middleware.ProtectAdminMiddleware'
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.static',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'common.context_processors.common',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
            'init_command': 'SET storage_engine=INNODB,'
                            'character_set_connection=utf8,'
                            'collation_connection=utf8_unicode_ci',
            'charset': 'utf8',
            'use_unicode': True,
        }
    },
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es-PE'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

GRAPPELLI_ADMIN_TITLE = 'Wunderman Phantasia Admin'

CORS_ORIGIN_ALLOW_ALL = False

BASE_URL = ''

# SABMiller module specific config
# SABMILLER_API_USER = ''
# SABMILLER_API_TOKEN = ''
# SABMILLER_SERVICE_URL = ''
# SABMILLER_CAMPAIGN = ''
# SABMILLER_BRAND = ''
# SABMILLER_FORMID = ''
