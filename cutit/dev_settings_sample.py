from .base import *

DEBUG = True

BASE_URL = "http://cutit.tk/"

ALLOWED_HOSTS = []

SECRET_KEY = os.environ.get('SECRET_KEY', '$c6wtefwk+awg8wdwd$0zq6$6cc8u740xr#%)*@1hnj4pm3@e0z')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME', "cutit"),
        'USER': os.environ.get('USER_NAME', "cutit"),
        'PASSWORD': os.environ.get('PASSWORD', "cutit"),
        'HOST': os.environ.get('HOST_NAME', "localhost"),
        'PORT': os.environ.get('PORT', "3306"),
    }
}
