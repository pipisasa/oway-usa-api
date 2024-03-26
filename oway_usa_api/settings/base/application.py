# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MY_APPS = [
    'apps.users.apps.UsersConfig',
    'apps.categories.apps.CategoriesConfig',
    'apps.catalog_sites.apps.CatalogSitesConfig',
]

INSTALLED_APPS = [
    *DJANGO_APPS,
    *MY_APPS,
    'rest_framework',
    'corsheaders',
    'drf_yasg',
]