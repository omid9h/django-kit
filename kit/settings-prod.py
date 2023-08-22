from .settings import *  # noqa

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]

CORS_ALLOWED_ORIGINS = [
    # Add allowed origins here
]

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True
