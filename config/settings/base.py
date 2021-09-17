"""Base settings to build other settings files upon."""

import environ
import os

ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path('PokemonEc')

env = environ.Env()
environ.Env.read_env(os.path.join(ROOT_DIR, '.env'))

# Base
DEBUG = env.bool('DJANGO_DEBUG', False)

# Language and timezone

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# DATABASES
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

# URLs
ROOT_URLCONF = 'config.urls'


# Apps
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
]

THIRD_PARTY_APPS = [
    'rest_framework'
]
LOCAL_APPS = [
    
    'PokemonEC.pokeapi.apps.PokeapiConfig',
    'PokemonEC.command.apps.CommandConfig',
    'PokemonEC.evolution_chain_api.apps.EvolutionChainApiConfig'
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Passwords
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

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# Admin
ADMIN_URL = 'admin/'
ADMINS = [
    ("""Enmanuel Madrid""", 'EnmanuelAlx@gmail.com'),
]
MANAGERS = ADMINS


STATIC_ROOT = str(ROOT_DIR('staticfiles'))
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    str(APPS_DIR.path('static')),
]


