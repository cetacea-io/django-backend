from django.db import models

from category.models import Category, Tag

# class Category(models.Model):
    # thumbnail = models.ImageField()
    # title = models.CharField()
    # popularity = models.PositiveIntegerField()

    # def __str__(self):
    #     return self.title


# class Tag(models.Model):
#     title = models.CharField()

#     def __str__(self):
#         return self.title

class MainCategory(models.Model):
    category = models.OneToOneField(Category, on_delete=models.CASCADE, primary_key=True)
    thumbnail = models.ImageField(upload_to='images', default='', blank=True, null=True)