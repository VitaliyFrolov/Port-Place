import os
from pathlib import Path

from django_stubs_ext import monkeypatch
from dotenv import load_dotenv

monkeypatch()
load_dotenv()


# ======================================================================================================================
# BASE SETTINGS
# ======================================================================================================================

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = int(os.getenv("DEBUG"))  # type: ignore

ALLOWED_HOSTS: list[str] = os.environ.get("ALLOWED_HOSTS").split(" ")  # type: ignore

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
    "django_extensions",
    # applications
    "src.apps.users",
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

ROOT_URLCONF = "src.config.urls"

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

WSGI_APPLICATION = "src.config.wsgi.application"

# ======================================================================================================================
# DATABASE SETTINGS
# ======================================================================================================================

DATABASES = {
    "default": {
        "ENGINE": os.getenv("PG_ENGINE"),
        "NAME": os.getenv("PG_DATABASE"),
        "USER": os.getenv("PG_USER"),
        "PASSWORD": os.getenv("PG_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}

# ======================================================================================================================
# MORE SETTINGS
# ======================================================================================================================

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

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ======================================================================================================================
# CORS SETTINGS
# ======================================================================================================================

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ["*"]
CSRF_COOKIE_SECURE = False
