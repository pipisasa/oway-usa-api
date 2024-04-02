from django.db import models

from apps.categories.models import Category
from apps.countries.models import Country


class CatalogSite(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    logo = models.ImageField(upload_to='catalog_sites/')

    def __str__(self):
        return self.name