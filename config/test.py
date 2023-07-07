# flake8: noqa

from .settings import *

DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'TEST_NAME': ':memory:',
        'TEST_CHARSET': 'UTF8',
    }
}
