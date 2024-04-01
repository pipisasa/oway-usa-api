from django.contrib import admin

from apps.countries.models import Country


@admin.register(Country)
class AdminCountry(admin.ModelAdmin):
    list_display = ("id", "name")
