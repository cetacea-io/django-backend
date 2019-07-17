from django.db import models
from django.contrib.auth import get_user_model

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from organizations.models import Organization

class Authorable(models.Model):
    limit = models.Q(app_label = 'users', model = 'user') | models.Q(app_label = 'organizations', model = 'organization')
    author_content_type = models.ForeignKey(ContentType, limit_choices_to=limit, on_delete=models.CASCADE)
    author_object_id = models.PositiveIntegerField()
    author = GenericForeignKey('author_content_type', 'author_object_id')

    class Meta:
        abstract = True

class Timestampable(models.Model):
    creation_date   = models.DateTimeField(blank=True, null=True) # when the project was created in cetacea

    class Meta:
        abstract = True

class Comment(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        related_name='comments',
        blank=False,
        on_delete=models.CASCADE
    )
    content = models.TextField(blank=False, null=False)
    likes = models.ManyToManyField(
        get_user_model(),
        related_name="comments_liked",
        blank=True
    )
    published = models.DateTimeField(auto_now_add=True, auto_now=False)

class Picture(models.Model):
    content = models.ImageField(upload_to='images', default='', blank=True, null=True)


class Location(models.Model):
    text = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.text

class Place(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    location = models.ForeignKey(Location, blank=True, null=True, on_delete=models.CASCADE)
    owner = models.ForeignKey(Organization, blank=True, null=True, on_delete=models.CASCADE)
    pictures = models.ManyToManyField(Picture, blank=True)

    def __str__(self):
        return self.title

class DateAndTime(models.Model):
    text            = models.CharField(max_length=50, blank=True, null=True)
    creation_date   = models.DateTimeField(blank=True, null=True) # when the project was created in cetacea
    due_date        = models.DateTimeField(blank=True, null=True) # When the project should be done
    start_date      = models.DateTimeField(blank=True, null=True) # If the project will start in a specific date

    def __str__(self):
        return self.text

class CommonItem(Authorable,
                Timestampable):
    title           = models.CharField(max_length=60, blank=True, null=True)
    cover_image     = models.ImageField(upload_to='images', default='', blank=True, null=True)

    categories      = models.ManyToManyField('category.Category', related_name='%(app_label)s_%(class)s_related', blank=True)
    tags            = models.ManyToManyField('category.Tag', related_name='%(app_label)s_%(class)s_related', blank=True)

    # cost            = models.DecimalField(max_digits=6, decimal_places=2)
    quick_desc      = models.CharField(max_length=255, blank=True, null=True)
    overview        = models.TextField(blank=True, null=True)

    # likes           = models.ManyToManyField(
    #                     get_user_model(),
    #                     related_name="events_liked",
    #                     blank=True
    #                 )

    # comments        = models.ManyToManyField(
    #                     Comment,
    #                     related_name='project',
    #                     blank=True
    #                 )

    # Dates and stuff
    date_and_time   = models.OneToOneField(DateAndTime, on_delete=models.CASCADE, null=True, blank=True)

    location        = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)

    #Wheter the project is published or still in creation process
    published       = models.BooleanField(default=False)

    class Meta:
        abstract = True

class CommonEvent(CommonItem):
    pass

    class Meta:
        abstract = True

class Event(CommonEvent):
    # classification # Que tipo de evento es -> obra de teatro, club de coro, club de lectura, presentacion, etc.
    # area # puede ser la categoria
    pass
    

class TeatherPlay(Event):
    pass