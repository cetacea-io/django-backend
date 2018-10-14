from django.db import models
from django.contrib.auth import get_user_model

# class Event(models.Model):


# class Course(models.Model):
#     title = models.CharField(max_length=100, blank=False)
#     category = models.
#     date = models.DateTimeField()
    
#     def __str__(self):
#         return self.title


# class Member(models.Model):
#     user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
#     ROLE_CHOICES = (
#         (u'1', u'Administrator'),
#         (u'2', u'Content'),
#         (u'3', u''),
#     )
#     role = models.CharField(max_length=1, choices=ROLE_CHOICES)

#     def __str__(self):
#         return self.user #TODO: get username of the user


# class Organization(models.Model):
#     title = models.CharField(max_length=100, blank=False)
#     members = models.ManyToManyField(Member,)

#     def __str__(self):
#         return self.title