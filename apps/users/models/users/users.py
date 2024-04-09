import random
import string

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from .custom_manager import CustomUserManager


def generate_unique_id(user_id):
    random_letters = ''.join(random.choices(string.ascii_uppercase, k=2))
    formatted_user_id = str(user_id).zfill(4)
    unique_id = f'{random_letters}{formatted_user_id}'
    return unique_id


class User(AbstractBaseUser, PermissionsMixin):
    unique_id = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField('email address', unique=True)
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
        if not self.unique_id:
            self.unique_id = generate_unique_id(self.id)
        super().save(*args, **kwargs)