from django.db import models
from django.contrib.auth import get_user_model
# from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    user            = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='images', blank=True, null=True)
    # phone         = PhoneNumberField(blank=True)
    bio             = models.TextField(null=True, blank=True)
    is_public       = models.BooleanField(default=True)
    interests       = models.ManyToManyField(
                        'category.Category',
                        related_name='users_interested',
                        blank=True,
                    )

    def __str__(self):
        return f'{self.user.username} Profile'