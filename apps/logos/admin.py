from django.contrib import admin

from apps.logos.models import Logo


@admin.register(Logo)
class AdminUsers(admin.ModelAdmin):
    list_display = ("id", "logo", "link")
