from django.db import models
from apps.users.models import User


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField('email address', blank=True, null=True)
    front_image = models.ImageField(upload_to='passport_front_images/', blank=True, null=True)
    back_image = models.ImageField(upload_to='passport_back_images/', blank=True, null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)