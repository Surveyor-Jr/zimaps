"""
Django settings for zimaps project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import django_heroku
import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

# configurations for the PostGIS Extension in the Postgresql Database

 
if os.name == 'nt':
     import platform
     OSGEO4W = r"C:\OSGeo4W"
     if '64' in platform.architecture()[0]:
         OSGEO4W += "64"
     assert os.path.isdir(OSGEO4W), "Directory does not exist: " + OSGEO4W
     os.environ['OSGEO4W_ROOT'] = OSGEO4W
     os.environ['GDAL_DATA'] = OSGEO4W + r"\share\gdal"
     os.environ['PROJ_LIB'] = OSGEO4W + r"\share\proj"
     os.environ['PATH'] = OSGEO4W + r"\bin;" + os.environ['PATH']


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'users.apps.UsersConfig',
    'crispy_forms',
    'leaflet',
    'collector.apps.CollectorConfig',
    'careers.apps.CareersConfig',
    'django_summernote',
    # Social Login
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google', # Login via Google
    'allauth.socialaccount.providers.github',
    'django_cleanup.apps.CleanupConfig', # automatically clean-up old files when deleted
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

ROOT_URLCONF = 'zimaps.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates/'],
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

WSGI_APPLICATION = 'zimaps.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER_NAME'),
        'HOST': env('DATABASE_HOST'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'PORT': env('DATABASE_PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Harare'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# Media Management 
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/') 

# allows to load iframe from same hostname 
X_FRAME_OPTIONS = 'SAMEORIGIN'
"""
# configurations for Leaflet Maps
LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (-19.0154, 29.1549), 
    'DEFAULT_ZOOM': 3,
    'MAX_ZOOM': 20,
    'MIN_ZOOM': 3,
    'SCALE': 'both',
    'ATTRIBUTION_PREFIX': 'SurveyorJr'
}
"""

# Crispy-Forms Configuration
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Login Configurations
LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'

# SummerNote theme
SUMMERNOTE_THEME = 'bs4'

django_heroku.settings(locals())

# setting up email 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' 
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "matingonk@gmail.com"  #replace this with your email
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD') 

# Speicify the AuthBackends 
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

AUTH_PROFILE_MODULE = 'users.Profile'

SITE_ID = 2

# Enable Email scope to receive user's email address after successfull login
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': [
            'profile',
            'email',
            'username',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}