from django.contrib import admin

from apps.catalog_sites.models import CatalogSite


@admin.register(CatalogSite)
class AdminCatalogSite(admin.ModelAdmin):
    list_display = ["id", "name"]
