from django.contrib import admin

from apps.cities.models import City


@admin.register(City)
class AdminCity(admin.ModelAdmin):
    list_display = ('id', 'name')
