from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='contacts')
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    email = models.EmailField()
    unit = models.CharField(max_length=255)

    def __str__(self):
        return self.name