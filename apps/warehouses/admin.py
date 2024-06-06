from django.contrib import admin

from apps.warehouses.models import (
    WarehouseProduct,
    Status,
    StatusPayment,
    Warehouse,
)


@admin.register(WarehouseProduct)
class AdminWarehouseProduct(admin.ModelAdmin):
    list_display = ('id', 'name', 'status')


@admin.register(Warehouse)
class AdminWarehouse(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Status)
class AdminStatus(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(StatusPayment)
class AdminStatusPayment(admin.ModelAdmin):
    list_display = ('id', 'name')
