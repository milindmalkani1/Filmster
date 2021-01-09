from filmster.settings.base import *


DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'filmster',
        'USER': 'postgres',
        'PASSWORD': 'imagesbazaar2610',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
