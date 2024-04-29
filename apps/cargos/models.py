from django.db import models


class Cargo(models.Model):
    arrived = models.CharField(max_length=50, null=True, blank=True)
    cargo = models.CharField(max_length=255, null=True, blank=True)

    update_date = models.CharField(max_length=50, null=True, blank=True)
    parcel_collection = models.CharField(max_length=50, null=True, blank=True)
    next_package = models.CharField(max_length=50, null=True, blank=True)