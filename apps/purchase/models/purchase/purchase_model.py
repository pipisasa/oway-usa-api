from datetime import datetime

from django.db import models

from oway_usa_api import settings


class Purchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField(blank=False, null=False)
    full_name = models.CharField(max_length=255, blank=False, null=False)
    url = models.URLField(blank=False, null=False)
    name_of_purchase = models.CharField(max_length=255, blank=False, null=False)
    count = models.IntegerField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    telegram = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    purchase_image = models.ImageField(upload_to='purchase_image/', blank=False, null=False)
    purchase_image_2 = models.ImageField(upload_to='purchase_image/', blank=True, null=True)

    payment_confirmation = models.ImageField(blank=True, null=True, upload_to='purchase_payment_confirmation')
    price = models.IntegerField(blank=True, null=True)

    created_at = models.DateTimeField(default=datetime.now)
