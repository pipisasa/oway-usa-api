# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
import os

from .base import BASE_DIR

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join('static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join('media')