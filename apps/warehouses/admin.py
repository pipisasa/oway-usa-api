from django.contrib import admin

from apps.warehouses.models import Warehouse, Status


@admin.register(Warehouse)
class AdminWarehouse(admin.ModelAdmin):
    list_display = ('id', 'name', 'status')


@admin.register(Status)
class AdminStatus(admin.ModelAdmin):
    list_display = ('id', 'name')
