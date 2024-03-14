import random

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from .custom_manager import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField('email address', unique=True)
    password = models.CharField(max_length=255, null=False, blank=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    activation_code = models.CharField(max_length=20, blank=True)

    address = models.CharField(max_length=255)

    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    is_banned = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=timezone.now, editable=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email}'

    def create_activation_code(self):
        code = random.randint(100000, 999999)
        self.activation_code = code
        self.save()

    def save(self, *args, **kwargs):
        if self.email:
            self.email = self.email.lower()
        super(User, self).save(*args, **kwargs)