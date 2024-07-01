from datetime import datetime

from django.db import models

from apps.countries.models import Country
from .status import Status
from .status_payment import StatusPayment
from .warehouse import Warehouse
from apps.address.models import Address


class WarehouseProduct(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, blank=True, null=True, related_name='products')
    name = models.CharField(max_length=255)
    country_of_origin = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, related_name='origin_warehouseproducts')
    country_of_destination = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, related_name='destination_warehouseproducts')
    weight = models.IntegerField(null=True, blank=True)
    length = models.CharField(max_length=255, blank=True, null=True)
    width = models.CharField(max_length=255, blank=True, null=True)
    height = models.CharField(max_length=255, blank=True, null=True)
    track_number = models.CharField(max_length=50)
    comments = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    status_many = models.BooleanField(default=False)
    status_payment = models.ForeignKey(StatusPayment, on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(verbose_name="цена", null=True, blank=True)

    image = models.ImageField(upload_to='warehouse_product/', null=True, blank=True)
    url = models.URLField(blank=True, null=True)
    articul = models.CharField(max_length=255, blank=True, null=True)

    unique_id_user = models.CharField(max_length=255)

    date_sent = models.CharField(max_length=50, null=True, blank=True)
    date_arrived = models.CharField(max_length=50, null=True, blank=True)

    is_parcels = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

