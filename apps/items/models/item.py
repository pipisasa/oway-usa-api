from django.db import models
from .category import Category


class Item(models.Model):
    text = models.TextField()
    item_category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    publication_date = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=255)

    class Meta:
        ordering = ('-publication_date',)

    def __str__(self):
        return self.text