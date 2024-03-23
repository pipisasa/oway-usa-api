from django.contrib import admin

from apps.notifications.models.notifications.mail_box import MailBox
from apps.notifications.models.notifications.notifications import Notifications


@admin.register(MailBox)
class AdminUsers(admin.ModelAdmin):
    list_display = ("id", "user", "notification", "status")


@admin.register(Notifications)
class AdminUsers(admin.ModelAdmin):
    list_display = ("id", "title")
