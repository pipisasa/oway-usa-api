from django.contrib import admin

from apps.cargos.models import Cargo


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cargo', 'arrived')
