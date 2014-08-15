import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'r269$heh9at2cot+5l$*$4&xzwsfbbg0&&^prr+e&oh)_4-+ga'
DEBUG = True
TEMPLATE_DEBUG = True
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_ROOT = os.path.join(BASE_DIR, ".static")
STATIC_URL = '/static/'
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]
ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.humanize',
    'storages',
    'bakery',
    'calaccess',
    'campaign_finance',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'campaign_finance',
        'USER': 'root',
        'PASSWORD': 'mysql',
        'HOST': '',
        'PORT': '3306',
        'OPTIONS': {
            'local_infile': 1,
        }
    }
}

BUILD_DIR = os.path.join(BASE_DIR, 'build')

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'

try:
    from settings_local import *
except ImportError:
    pass
