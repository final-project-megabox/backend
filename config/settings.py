"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'oqtnw$$mwoby8jpy1yqbe29+a4qv31y=)ab055)+xmj379!7e('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'rest_framework',
    'rest_framework_swagger',
    'rest_framework.authtoken',
    'debug_toolbar',
    'django_extensions',
    'database',
    'drf_yasg',
    'multiselectfield',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'layout')],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# import secret
# DATABASES = {
#     'default': {
#         'ENGINE': secret.database['ENGINE'],
#         'NAME': secret.database['NAME'],
#         'USER': secret.database['USER'],
#         'PASSWORD': secret.database['PASSWORD'],
#         'HOST': secret.database['HOST'],
#         'PORT': secret.database['PORT'],
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = '/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

INSTERNAL_IPS = ['127.0.0.1']

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
}

# REST_FRAMEWORK = {
#     'DEFAULT_RENDERER_CLASSES': (
#         'rest_framework.renderers.JSONRenderer',
#     ),
#     # 'DEFAULT_PERMISSION_CLASSES': (
#     #     'rest_framework.permissions.IsAuthenticated',
#     # ),
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.TokenAuthentication',
#     ),
#     'DEFAULT_FILTER_BACKENDS': (
#         'django_filters.rest_framework.DjangoFilterBackend',
#         'rest_framework.filters.SearchFilter',
#     )
# }

REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

JWT_AUTH = {
    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'config.jwt.jwt_response_payload_handler',
    'JWT_ALGORITHM': 'HS256',
    'JWT_ALLOW_REFRESH': True,  # Token Refresh 가능 여부
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),  # Token 만료시간
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=3),  # Token Refresh 가능 시간
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        "api_key": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
        }
    }
}

import secret
AWS_ACCESS_KEY_ID = secret.settings['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = secret.settings['AWS_SECRET_ACCESS_KEY']
AWS_REGION = secret.settings['AWS_REGION']
AWS_STORAGE_BUCKET_NAME = secret.settings['AWS_STORAGE_BUCKET_NAME']
AWS_S3_CUSTOM_DOMAIN = secret.settings['AWS_S3_CUSTOM_DOMAIN']
AWS_S3_SECURE_URLS = secret.settings['AWS_S3_SECURE_URLS']

AWS_S3_OBJECT_PARAMETERS = secret.settings['AWS_S3_OBJECT_PARAMETERS']
AWS_DEFAULT_ACL = secret.settings['AWS_DEFAULT_ACL']
AWS_LOCATION = secret.settings['AWS_LOCATION']
STATICFILES_STORAGE = secret.settings['STATICFILES_STORAGE']

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = [
    'http://google.com',
    'http://hostname.example.com',
    'http://localhost:8000',
    'http://localhost:4200',
    'http://127.0.0.1:9000',
]

AUTH_USER_MODEL = 'accounts.User'
