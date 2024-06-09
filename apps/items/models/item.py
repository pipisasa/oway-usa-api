from django.db import models


class Item(models.Model):
    text = models.TextField()
    category = models.CharField(max_length=255)
    color = models.CharField(max_length=100)
    publication_date = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=255)

    class Meta:
        ordering = ('-publication_date',)

    def __str__(self):
        return self.text