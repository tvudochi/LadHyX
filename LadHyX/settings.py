"""
Django settings for LadHyX project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys
from socket import gethostname

gettext = lambda s: s

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(os.path.join(BASE_DIR, 'LadHyX', 'templates'))
# print(BASE_DIR)
# /home/toai/Developpement/LadHyX/LadHyX

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = ['*']
CHANNEL = {}
if gethostname() == 'alix':
    DEBUG = True
    # TEMPLATE_DEBUG = True
    PROG = BASE_DIR + '/publications/Prog/search-pub-rp-stdin.exe'
    OUVRAGES = BASE_DIR + '/publications/Data/publi.bo.dat'
    THESES = BASE_DIR + '/publications/Data/publi.ph.dat'
    INFO = BASE_DIR + '/publications/Data/info-publi.dat'

if gethostname() == 'quasi':
    DEBUG = False
    TEMPLATE_DEBUG = False
    PROG = '/srv/www/Django-publications/Prog/search-pub-rp-stdin.exe'
    OUVRAGES = '/srv/www/Django-publications/Data/publi.bo.dat'
    THESES = '/srv/www/Django-publications/Data/publi.ph.dat'
    INFO = '/srv/www/Django-publications/Data/info-publi.dat'


# Application definition

INSTALLED_APPS = [
    # 'livereload',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'LadHyX',
    'personnel',
    'evenement',
    'mathfilters',
    'publications',
    'mutltimedia',
]

if DEBUG is True:
    INSTALLED_APPS.insert(0, 'livereload')

# LIVERELOAD_HOST = '127.0.0.1'
# LIVERELOAD_PORT = '8000'
# Pour Debug Mode dans template base.html
INTERNAL_IPS = (
    '0.0.0.0',
    '127.0.0.1',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'livereload.middleware.LiveReloadScript',
]

ROOT_URLCONF = 'LadHyX.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'LadHyX', 'templates', 'EnergieEtTransport'),
                 os.path.join(BASE_DIR, 'LadHyX', 'templates', 'Environnement'),
                 os.path.join(BASE_DIR, 'LadHyX', 'templates', 'DesignEtSociete'),
                 os.path.join(BASE_DIR, 'LadHyX', 'templates', 'DesignEtSociete', 'ArtEtScience'),
                 os.path.join(BASE_DIR, 'LadHyX', 'templates', 'DesignEtSociete', 'Sportsphysics'),
                 os.path.join(BASE_DIR, 'LadHyX', 'templates', 'BiomecaEtSante'),
                 os.path.join(BASE_DIR, 'LadHyX', 'templates', 'evenement')
                 ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                # 'django.core.context_processors.i18n',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'LadHyX.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': '',

    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('fr', gettext('French')),
    ('en', gettext('English')),
)

LOCALE_PATHS = [

]
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'LadHyX', 'collectstatic')

MEDIA_URL = '/media/'

# MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')
MEDIA_ROOT = os.path.join(BASE_DIR, 'LadHyX', 'media')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'LadHyX', 'static'),
)



