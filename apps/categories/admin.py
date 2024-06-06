from django.contrib import admin

from apps.categories.models import Category


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ("id", "name")
