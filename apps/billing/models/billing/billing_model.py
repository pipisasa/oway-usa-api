from django.db import models

from oway_usa_api import settings


class Billing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, null=False, blank=False)
    number = models.IntegerField(null=False, blank=False)
    end_date = models.CharField(max_length=255, null=False, blank=False)
    cvv = models.IntegerField(null=False, blank=False)