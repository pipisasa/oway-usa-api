from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    link = models.URLField(null=False, blank=False)
    image = models.ImageField(upload_to='products/', null=False, blank=False)
