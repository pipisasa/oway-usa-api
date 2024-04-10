from django.db import models


class StatusPayment(models.Model):
    name = models.CharField(max_length=255)