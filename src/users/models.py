from django.db import models

from django.contrib.auth.models import AbstractUser

# from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    # picture = models.ImageField(upload_to='images', blank=True, null=True)
    picture = models.URLField()
    bio = models.TextField(null=True, blank=True)
    # phone = PhoneNumberField(blank=True)
    public_profile = models.BooleanField(default=True)


    def __str__(self):
        return self.email