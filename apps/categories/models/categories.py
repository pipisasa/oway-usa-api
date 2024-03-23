from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    codename = models.CharField(max_length=255, null=True, blank=True, unique=True)
    icon = models.ImageField(upload_to='category_icons/', null=False, blank=False)