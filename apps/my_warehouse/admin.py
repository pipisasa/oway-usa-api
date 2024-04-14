from django.contrib import admin

from apps.my_warehouse.models import MyWarehouse


@admin.register(MyWarehouse)
class AdminUsers(admin.ModelAdmin):
    list_display = ("id", "warehouse", "tracking_number", "courier_service")
