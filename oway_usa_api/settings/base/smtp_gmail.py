import os

from dotenv import load_dotenv

load_dotenv()

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
_email_backend = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_ACCOUNTS = {
    "base": {
        'EMAIL_BACKEND': _email_backend,
        'EMAIL_USER': os.getenv("EMAIL_HOST_USER"),
        'EMAIL_PASSWORD': os.getenv("EMAIL_HOST_PASSWORD"),
    }
}