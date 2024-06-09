from datetime import datetime

from django.db import models

from apps.countries.models import Country
from apps.cities.models import City


class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=50)
    mail = models.EmailField()
    phone_number = models.CharField(max_length=255)

    is_view = models.BooleanField(default=False)
    unit = models.CharField(max_length=255, blank=True, null=True)
    icon = models.ImageField(upload_to='warehouse/', null=True, blank=True)

    created_at = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.name