"""
Django settings for cloudstorage project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

from .emailsettings import SET_EMAIL_USE_TLS, SET_EMAIL_HOST, SET_EMAIL_HOST_USER,\
    SET_EMAIL_HOST_PASSWORD, SET_EMAIL_PORT, SET_EMAIL_BACKEND, SET_DEFAULT_FROM_EMAIL
# Email settings 
EMAIL_USE_TLS = SET_EMAIL_USE_TLS
EMAIL_HOST = SET_EMAIL_HOST
EMAIL_HOST_USER = SET_EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = SET_EMAIL_HOST_PASSWORD
EMAIL_PORT = SET_EMAIL_PORT
EMAIL_BACKEND = SET_EMAIL_BACKEND
DEFAULT_FROM_EMAIL = SET_DEFAULT_FROM_EMAIL

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b3(=423c%5&!z3c@&673k0nby#d@(lbzh78a_+u#se&izl-g4h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainapp',
    'proxyapp',
    'controllerapp',
    'clientapp',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cloudstorage.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'assets/templates')],
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

WSGI_APPLICATION = 'cloudstorage.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cloudstorage',
        'Host': 'localhost',
        'USER': 'root',
        'PASSWORD' : "",
        'PORT' : '3306',
        'OPTIONS': {
            'init_command' : "SET sql_mode = 'STRICT_TRANS_TABLES'"
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATIC_URL = 'static/'
# STATICFILES_DIRS=os.path.join(BASE_DIR,'assets/static'),

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

# cloud
# step : 1
AWS_ACCESS_KEY_ID = 'AKIARAA7CSNOSJNU6KF6' 
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'priya-tweakycloud-project'
AWS_S3_CUSTOM_DOMAIN='%s.s3.amazonaws.com'% AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
 'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
STATICFILES_DIRS = [
 os.path.join(BASE_DIR, 'assets/static'),
]
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


# step : 2
STATICFILES_DIRS = [
 os.path.join(BASE_DIR, 'assets/static'),
]
AWS_ACCESS_KEY_ID = 'AKIARAA7CSNOSJNU6KF6' 
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'priya-tweakycloud-project'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
 'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
DEFAULT_FILE_STORAGE = 'cloudstorage.storage_backends.MediaStorage'


# step : 3
AWS_ACCESS_KEY_ID = 'AKIARAA7CSNOSJNU6KF6' 
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'priya-tweakycloud-project'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
 'CacheControl': 'max-age=86400',
}
AWS_STATIC_LOCATION = 'static'
STATICFILES_STORAGE = 'cloudstorage.storage_backends.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)
AWS_PUBLIC_MEDIA_LOCATION = 'media/public'
DEFAULT_FILE_STORAGE = 'cloudstorage.storage_backends.PublicMediaStorage'
AWS_PRIVATE_MEDIA_LOCATION = 'media/private'
PRIVATE_FILE_STORAGE = 'cloudstorage.storage_backends.PrivateMediaStorage'



# AWS_ACCESS_KEY_ID = 'AKIARAA7CSNOSJNU6KF6' 
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'priya-tweakycloud-project'
# AWS_S3_CUSTOM_DOMAIN='%s.s3.amazonaws.com'% AWS_STORAGE_BUCKET_NAME
# AWS_S3_OBJECT_PARAMETERS = {
#  'CacheControl': 'max-age=86400',
# }
# AWS_STATIC_LOCATION = 'static'
# DEFAULT_FILE_STORAGE = 'cloudstorage.storage_backends.PublicMediaStorage' 
# AWS_PRIVATE_MEDIA_LOCATION = 'media/private'
# PRIVATE_FILE_STORAGE = 'cloudstorage.storage_backends.PrivateMediaStorage'

# STATICFILES_DIRS = [
#  os.path.join(BASE_DIR, 'assets/static'),
# ]

# STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# AWS_QUERYSTRING_AUTH = False

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

AWS_S3_REGION_NAME = 'ap-south-1' #change to your region
AWS_S3_SIGNATURE_VERSION = 's3v4'
# AWS_ACCESS_KEY_ID = 'AKIARAA7CSNOTMHJRJDD' 
# AWS_SECRET_ACCESS_KEY = 'nnXwEkktsC4Otj3FK48HpfPYLpALfgKJoQKrNEZr'
# AWS_STORAGE_BUCKET_NAME = 'tweakyhybridcloudstorageforvideofiles'
# AWS_QUERYSTRING_AUTH = False

