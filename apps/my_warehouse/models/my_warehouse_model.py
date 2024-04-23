from django.db import models

from oway_usa_api import settings


class MyWarehouse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    warehouse = models.CharField(max_length=255, null=False, blank=False)
    tracking_number = models.CharField(max_length=255, null=False, blank=False)
    courier_service = models.CharField(max_length=255, null=False, blank=False)
    comments = models.TextField(max_length=500, null=False, blank=False)
