from django.contrib import admin

from apps.clients_outside_of_illinois.model import OutsideOfIllinois


@admin.register(OutsideOfIllinois)
class AdminUsers(admin.ModelAdmin):
    list_display = ("id", "full_name", "phone_number", "status", "email", "telegram", "whatsapp")
