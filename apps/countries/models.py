from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255)
    codename = models.CharField(max_length=255, null=True, blank=True, unique=True)
    icon = models.ImageField(upload_to='country_icons/', null=False, blank=False)