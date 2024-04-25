from django.db import models


class Logo(models.Model):
    logo = models.ImageField(upload_to='logos/')
    link = models.URLField(null=False, blank=False)

