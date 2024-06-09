from django.contrib import admin

from apps.items.models import Item


@admin.register(Item)
class AdminItem(admin.ModelAdmin):
    list_display = ('id', 'category',)
