from django.db import models

from oway_usa_api import settings
from apps.warehouses.models import Warehouse

from apps.countries.models import Country


class MyWarehouse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, blank=True, null=True)
    tracking_number = models.CharField(max_length=255, null=False, blank=False)
    courier_service = models.CharField(max_length=255, null=False, blank=False)
    comments = models.TextField(max_length=500, null=False, blank=False)
    country_of_origin = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, related_name='origin_my_warehouseproducts')
    country_of_destination = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, related_name='destination_my_warehouseproducts')
