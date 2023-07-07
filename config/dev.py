# flake8: noqa

from .settings import *

DEBUG = True

SECRET_KEY = env('SECRET_KEY')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'OPTIONS': {
            'server_side_binding': True,
        },
        'NAME': env('DB_NAME', default='xxx_dev'),
        'USER': env('DB_USER', default='postgres'),
        'PASSWORD': env('DB_PASSWORD', default='postgres'),
        'HOST': env('DB_HOST', default='localhost'),
        'PORT': env('DB_PORT', default=5432)
    }
}

INSTALLED_APPS.extend([
    'drf_spectacular'
])

REST_FRAMEWORK.update({
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
})

SPECTACULAR_SETTINGS = {
    'TITLE': 'drf-starter',
    'DESCRIPTION': 'Project description',
    'VERSION': '0.1.0',
    'SERVE_INCLUDE_SCHEMA': False,
}
