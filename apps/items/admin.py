from django.contrib import admin

from apps.items.models import Item, Category


@admin.register(Item)
class AdminItem(admin.ModelAdmin):
    list_display = ('id', 'item_category',)


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'name',)
