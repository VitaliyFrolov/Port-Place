import os
from pathlib import Path

from django_stubs_ext import monkeypatch
from dotenv import load_dotenv

load_dotenv()
monkeypatch()

# ======================================================================================================================
# BASE SETTINGS
# ======================================================================================================================

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-)po9cx#hgi5*=^=f5zhpe-au6!nk0$a)z=ax9o)z83(s^fuhcr"

DEBUG = True

ALLOWED_HOSTS = []

# ======================================================================================================================
# APPS SETTINGS
# ======================================================================================================================

INSTALLED_APPS = [
    # base
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    # third-party
    "rest_framework",
    "django_extensions",
    # applications
    "server.apps.tables.apps.TablesConfig",
    "server.apps.reservations.apps.ReservationsConfig",
    "server.apps.residents.apps.ResidentsConfig",
]

# ======================================================================================================================
# MIDDLEWARE SETTINGS
# ======================================================================================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ======================================================================================================================
# ROOT URL SETTINGS
# ======================================================================================================================

ROOT_URLCONF = "server.config.urls"

# ======================================================================================================================
# TEMPLATES SETTINGS
# ======================================================================================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ======================================================================================================================
# WSGI SETTINGS
# ======================================================================================================================

WSGI_APPLICATION = "server.config.wsgi.application"

# ======================================================================================================================
# DATABASE SETTINGS
# ======================================================================================================================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ======================================================================================================================
# MORE SETTINGS
# ======================================================================================================================

API_PREFIX: str = os.environ.get("API_PREFIX", "api/v1")

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "ru"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True


USE_TZ = True

STATIC_URL = "static/"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ======================================================================================================================
# CORS SETTINGS
# ======================================================================================================================

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ["*"]
CSRF_COOKIE_SECURE = False
