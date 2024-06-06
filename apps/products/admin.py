from django.contrib import admin
from apps.products.models import Products


@admin.register(Products)
class AdminUsers(admin.ModelAdmin):
    list_display = ("id", "title")
