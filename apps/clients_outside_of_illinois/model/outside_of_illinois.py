from django.db import models


class OutsideOfIllinois(models.Model):
    full_name = models.CharField(max_length=255, null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    phone_number = models.CharField(max_length=255, null=False, blank=False)
    cargo_weight = models.IntegerField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    telegram = models.CharField(max_length=255, null=False, blank=False)
    whatsapp = models.CharField(max_length=255, null=False, blank=False)

    status = models.BooleanField(default=False)
