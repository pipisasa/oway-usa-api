from datetime import datetime

from django.db import models

from apps.countries.models import Country
from .status import Status
from .status_payment import StatusPayment


class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    weight = models.FloatField(default=0)
    track_number = models.CharField(max_length=50)
    comments = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    status_payment = models.ForeignKey(StatusPayment, on_delete=models.SET_NULL, null=True)
    price = models.FloatField(default=0)
    unique_id_user = models.CharField(max_length=255)
    image = models.ImageField(upload_to='warehouse/', null=True, blank=True)
    url = models.URLField(blank=True, null=True)
    articul = models.CharField(max_length=255, default="default", blank=False, null=False)
    price = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(default=0,blank=False, null=False)
    color = models.CharField(default="default-color", max_length=255, blank=False, null=False)

    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

