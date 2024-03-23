from django.db import models

from apps.categories.models import Category


class CatalogSite(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    logo = models.ImageField(upload_to='catalog_sites/')

    def __str__(self):
        return self.name