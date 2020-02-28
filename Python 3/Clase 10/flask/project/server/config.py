# project/server/config.py

import os

basedir = os.path.abspath(os.path.dirname(__file__))

POSTGRES_URL = 'salt.db.elephantsql.com'
POSTGRES_USER = 'qhpmvcxf'
POSTGRES_PW = 'KVyxuSnUjHqmS8cv87HmKljukR7IKAXA'
POSTGRES_DB = 'qhpmvcxf'

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER, pw=POSTGRES_PW,
                                                               url=POSTGRES_URL, db=POSTGRES_DB)

class BaseConfig(object):
    """Base configuration."""

    APP_NAME = 'Skeleton' #os.getenv("APP_NAME", "Flask Skeleton")
    BCRYPT_LOG_ROUNDS = 4
    DEBUG_TB_ENABLED = False
    SECRET_KEY = 'asdasdasd'#os.getenv("SECRET_KEY", "my_precious")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_DATABASE_URI = DB_URL


class TestingConfig(BaseConfig):
    """Testing configuration."""

    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST_URL", "sqlite:///")
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configuration."""

    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_DATABASE_URI = DB_URL
    WTF_CSRF_ENABLED = True
