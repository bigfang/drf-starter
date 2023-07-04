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
