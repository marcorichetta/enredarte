"""
Django settings for enredarte project.
"""

import os
from typing import List
import environ
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .jazzmin_settings import JAZZMIN_SETTINGS, JAZZMIN_UI_TWEAKS

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# .../enredarte/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env(
    # Set casting, default value for production
    DEBUG=(bool, False)
)

# reading .env file
env_file = os.path.join(BASE_DIR, ".env")
if os.path.exists(env_file):
    environ.Env.read_env(env_file)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a space between each.
# For example: 'ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'
ALLOWED_HOSTS: List[str] = env.str("ALLOWED_HOSTS").split(" ")

INSTALLED_APPS: List[str] = [
    # Django
    "dal",
    "dal_select2",
    "jazzmin",
    "django.contrib.admindocs",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",  # #Disable Django static file server during DEVELOPMENT
    "django.contrib.staticfiles",
    # 3rd party
    "crispy_forms",
    "django_extensions",
    "django_tables2",
    "widget_tweaks",
    "stronghold",
    "imagefield",
    # My apps
    "core",
    "users",
    "variables",
    "productos",
    "clientes",
    "proveedores",
    "pedidos",
    "compras",
    "calendario",
    "reportes",
]

MIDDLEWARE: List[str] = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "stronghold.middleware.LoginRequiredMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# DJANGO-DEBUG-TOOLBAR CONFIGS
# ------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
# https://docs.djangoproject.com/en/dev/ref/settings/#internal-ips

# Enable the debug toolbar only in DEBUG mode.
if False:
    INSTALLED_APPS.append("debug_toolbar")
    MIDDLEWARE.insert(1, "debug_toolbar.middleware.DebugToolbarMiddleware")
    INTERNAL_IPS = ["172.22.0.1", "localhost", "127.0.0.1"]

    DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda _request: DEBUG}


ROOT_URLCONF = "enredarte.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "enredarte.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {"default": env.db_url("DATABASE_URL")}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Logging
# https://docs.djangoproject.com/en/2.2/topics/logging

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "es-AR"

TIME_ZONE = "America/Argentina/Cordoba"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
# http://whitenoise.evans.io/en/stable/django.html#add-compression-and-caching-support
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"


# MEDIA
# ------------------------------------------------------------------------------
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# DJANGO-CRISPY-FORMS CONFIGS
# ------------------------------------------------------------------------------
# https://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = "bootstrap4"

# Override login redirect url
LOGIN_REDIRECT_URL = "core:choice-homepage"
LOGIN_URL = "login"
LOGOUT_REDIRECT_URL = "login"

AUTH_USER_MODEL = "users.CustomUser"

# DJANGO TABLES 2
# ------------------------------------------------------------------------------
DJANGO_TABLES2_TEMPLATE = "django_tables2/bootstrap4.html"

# DJANGO ImageField
# ------------------------------------------------------------------------------
IMAGEFIELD_FORMATS = {
    # image field path, lowercase
    "yourapp.yourmodel.image": {
        "square": ["default", ("crop", (200, 200))],
        "full": ["default", ("thumbnail", (800, 500))],
    }
}

# SENTRY
# ------------------------------------------------------------------------------
# sentry_sdk.init(
#     dsn=os.getenv("SENTRY_DSN"),
#     integrations=[DjangoIntegration()],
#     traces_sample_rate=1.0,
#     # If you wish to associate users to errors (assuming you are using
#     # django.contrib.auth) you may enable sending PII data.
#     send_default_pii=True,
# )

if DEBUG:
    try:
        from .local_settings import *
    except ModuleNotFoundError:
        pass
