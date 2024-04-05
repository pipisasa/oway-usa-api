from django.db import models


class Notifications(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    icon = models.ImageField(upload_to='notifications/', null=True, blank=True)
