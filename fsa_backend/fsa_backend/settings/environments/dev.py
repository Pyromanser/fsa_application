"""
This file contains all the settings that defines the development server.

SECURITY WARNING: don't run with debug turned on in production!
"""

from fsa_backend.settings.components import BASE_DIR
from fsa_backend.settings.components.base import env, MIDDLEWARE, INSTALLED_APPS

DEBUG = env("DJANGO_DEBUG", default=True)

# Email configuration
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"  # console
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "mailhog"
EMAIL_PORT = "25"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_SSL = False

ALLOWED_HOSTS = ["*"]

# Security
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
CORS_ORIGIN_ALLOW_ALL = True

STATIC_ROOT = BASE_DIR.joinpath("..", "staticfiles")
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
MEDIA_URL = "/media/"


DOMAIN = "localhost"
SCHEMA = "http"

INSTALLED_APPS += [
    "silk",
]

MIDDLEWARE += [
    "silk.middleware.SilkyMiddleware",
]

SILKY_PYTHON_PROFILER = True
SILKY_META = True
