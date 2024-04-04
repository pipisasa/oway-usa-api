from django.contrib import admin
from apps.purchase.models import Purchase


@admin.register(Purchase)
class AdminUsers(admin.ModelAdmin):
    list_display = ("id", "full_name", "telegram", "phone_number", "payment_confirmation")
