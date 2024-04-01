from django.db import models

from apps.countries.models import Country
from .status import Status


class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    weight = models.FloatField(default=0)
    track_number = models.CharField(max_length=50)
    comments = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    price = models.FloatField(default=0)
    unique_id_user = models.CharField(max_length=255)
    image = models.ImageField(upload_to='warehouse/', null=True, blank=True)

    def __str__(self):
        return self.name

