from django.db import models


class Purchase(models.Model):
    full_name = models.CharField(max_length=255, blank=False, null=False)
    url = models.URLField(blank=False, null=False)
    name_of_purchase = models.CharField(max_length=255, blank=False, null=False)
    articul = models.CharField(max_length=255, blank=False, null=False)
    count = models.IntegerField(blank=False, null=False)
    color = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    telegram = models.CharField(max_length=255, blank=False, null=False)
    phone_number = models.CharField(max_length=255, blank=False, null=False)
    purchase_image = models.ImageField(upload_to='purchase_image/', blank=False, null=False)

    payment_confirmation = models.ImageField(blank=True, null=True, upload_to='purchase_payment_confirmation')
    price = models.IntegerField(blank=True, null=True)

