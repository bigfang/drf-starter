from .settings import *

DEBUG = False

ALLOWED_HOSTS=['localhost']

SECRET_KEY = env('SECRET_KEY')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'OPTIONS': {
            'server_side_binding': True,
        },
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST', default='localhost'),
        'PORT': env('DB_PORT', default=5432)
    }
}
