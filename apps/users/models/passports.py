from django.db import models

from .users.users import User


class PassportFront(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    front_image = models.ImageField(upload_to='passport_front_images/')

    def __str__(self):
        return f'Passport front of {self.user.email}'


class PassportBack(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    back_image = models.ImageField(upload_to='passport_back_images/')

    def __str__(self):
        return f'Passport back of {self.user.email}'
