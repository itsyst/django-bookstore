from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-qewn-bz%peq236z^ehm1w)0lb2he!9&udqyf+#!_13ks2(s*ux'

# MIDDLEWARE += ['silk.middleware.SilkyMiddleware']
MIDDLEWARE.append('silk.middleware.SilkyMiddleware')


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'app.sqlite3',
    }
}