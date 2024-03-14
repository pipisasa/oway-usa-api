from django.contrib import admin

from apps.users import models


@admin.register(models.User)
class AdminUsers(admin.ModelAdmin):
    list_display = ("id", "email", "first_name", "last_name", "phone_number", "is_active", "is_admin")


@admin.register(models.PassportFront)
class AdminPassportFront(admin.ModelAdmin):
    list_display = ("id",)


@admin.register(models.PassportBack)
class AdminPassportBack(admin.ModelAdmin):
    list_display = ("id",)