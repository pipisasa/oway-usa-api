from django.contrib import admin
from apps.billing.models import Billing


@admin.register(Billing)
class AdminUsers(admin.ModelAdmin):
    list_display = ("id", "user", "full_name", "number", "end_date")
