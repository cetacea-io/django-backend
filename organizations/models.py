from django.db import models
from django.contrib.auth import get_user_model

class Member(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    ROLE_CHOICES = (
        (u'1', u'Administrator'),
        (u'2', u'Content'),
        (u'3', u''),
    )
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)

    def __str__(self):
        return self.user


class Organization(models.Model):
    title = models.CharField(max_length=100, blank=False)
    profile_picture = models.ImageField(upload_to='images', null=True)
    members = models.ManyToManyField(Member, blank=True)

    def __str__(self):
        return self.title