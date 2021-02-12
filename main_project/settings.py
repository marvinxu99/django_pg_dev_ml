"""
Django settings for main_project project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from decouple import config, Csv
# import django_heroku
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse_lazy

# Define custom user model
AUTH_USER_MODEL = 'accounts.User'

LOGIN_URL = reverse_lazy('accounts:login')
LOGIN_REDIRECT_URL = reverse_lazy('home')
LOGOUT_REDIRECT_URL = reverse_lazy('home')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROD_DEPLOY = config('PROD_DEPLOY', default=False, cast=bool)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

if PROD_DEPLOY:
    DEBUG=False
    ADMIN_NAME = config('ADMIN_NAME', default='Winter')
    ADMIN_EMAIL = config('ADMIN_EMAIL', default='winnpysoft@gmail.com')
    ADMINS = [(ADMIN_NAME, ADMIN_EMAIL)]
    DOMAIN = config('DOMAIN', default='PROD')
else:
    DOMAIN = config('DOMAIN', default='DEV')

DOMAIN_URL = config('DOMAIN_URL', default='http://localhost:8000')

#ALLOWED_HOSTS = ['winn.herokuapp.com', '127.0.0.1']
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
#    'whitenoise.runserver_nostatic',    # http://whitenoise.evans.io/en/stable/django.html
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'polls.apps.PollsConfig',
    'accounts.apps.AccountsConfig',
    'boards.apps.BoardsConfig',
    'catalog.apps.CatalogConfig',
    'core.apps.CoreConfig',
    'kbase.apps.KbaseConfig',
    'posts.apps.PostsConfig',
    'utils.apps.UtilsConfig',
    'itrac.apps.iTracConfig',
    'webgl.apps.WebglConfig',
    'payments.apps.PaymentsConfig',
    'budget.apps.BudgetConfig',
    'scan_n_pay.apps.ScannPayConfig',
    'books.apps.BooksConfig',
    'shop.apps.ShopConfig',

    # Third-party applications:
    'widget_tweaks',
#    'storages',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',    # http://whitenoise.evans.io/en/stable/
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',    # added for i18n, 2020.12.27
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'main_project.wsgi.application'

# Email backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = config('MY_GMAIL')
EMAIL_HOST_PASSWORD = config('MY_GMAIL_PASSWORD')
EMAIL_USE_SSL = True
EMAIL_PORT = 465

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# mysql wheels: https://www.lfd.uci.edu/~gohlke/pythonlibs/
# postgreSQL: https://docs.djangoproject.com/en/3.0/ref/databases/

DB_NAME = config('DB_NAME')
DB_USER = config('DB_USER')
DB_USER_PASSWD = config('DB_USER_PASSWD')
DB_HOST = config('DB_HOST')
DB_PORT = config('DB_PORT')
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }

    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'winn_dev2',
    #     'USER': 'winter',
    #     'PASSWORD': 'winter',
    #     'HOST': 'localhost',
    #     'PORT': '',
    #     # 'OPTIONS': {
    #     #     'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
    #     #     }
    # }

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_USER_PASSWD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en'
# LANGUAGE_CODE = 'zh-hans'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'US/Pacific'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('en', _('English')),
    ('fr', _('French')),
    ('zh-hans', u'简体中文'),
    ('zh-hant', u'繁體中文'),
]
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'conf/locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# STATICFILES_DIRS
# is used to include additional directories for collectstatic to look for.
# For example, by default, Django doesn't recognize /myProject/static/
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# STATIC_ROOT
# defines the single folder you want to collect all your static files into.
# While DEBUG=True, STATIC_ROOT does nothing. You even don't need to set it. Django looks for static
# files inside each app's directory (myProject/appName/static) and serves them automatically.
if PROD_DEPLOY:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATIC_URL = '/static/'
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATIC_URL = '/static/'

# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# http://whitenoise.evans.io/en/stable/django.html#storage-troubleshoot
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'


# MEDIA_ROOT is the folder where files uploaded using FileField will go.
if DEBUG:
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
else:
    MEDIA_URL = 'http://192.168.0.57/media/'
    MEDIA_ROOT = 'http://192.168.0.57/media/'

FILE_UPLOAD_DIR = os.path.join(BASE_DIR, 'uploaded_files')
GENERATED_BARCODE_DIR = os.path.join(BASE_DIR, 'generated_codes')

STRIPE_PUBLISHABLE_KEY = 'pk_test_LBnp367Zb5XklDLhtXFg1cgr00SIM9ArGv'
STRIPE_SECRET_KEY = config('STRIPE_SECRET_KEY')

# Oxford Dictionaries API
OXFORD_APP_ID = config('OXFORD_APP_ID', default='')
OXFORD_APP_KEY = config('OXFORD_APP_KEY', default='')


# Configure Django App for Heroku.
# django_heroku.settings(locals())
