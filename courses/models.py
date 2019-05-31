from django.db import models

from accounts.models import Profile

class Location(models.Model):
    text = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.text

class DateAndTime(models.Model):
    text            = models.CharField(max_length=50, blank=True, null=True)
    creation_date   = models.DateTimeField(blank=True, null=True) # when the project was created in cetacea
    due_date        = models.DateTimeField(blank=True, null=True) # When the project should be done
    start_date      = models.DateTimeField(blank=True, null=True) # If the project will start in a specific date

    def __str__(self):
        return self.text

class Cost(models.Model):
    pass

class CommonEvent(models.Model):
    title           = models.CharField(max_length=60, blank=True, null=True)
    cover_image     = models.ImageField(upload_to='images', default='', blank=True, null=True)
    author          = models.ForeignKey('organizations.Organization', on_delete=models.SET_NULL, null=True, blank=True)

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

    # Dates and stuff
    date_and_time   = models.OneToOneField(DateAndTime, on_delete=models.CASCADE, null=True, blank=True)

    location        = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)

    #Wheter the project is published or still in creation process
    published       = models.BooleanField(default=False)

    class Meta:
        abstract = True


class CourseClassification(models.Model):
    # Curso, Taller, Diplomado
    title = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title


class Course(CommonEvent):

    classification  = models.ForeignKey(CourseClassification, on_delete=models.CASCADE, null=False, blank=False)
    
    area            = models.CharField(max_length=60, blank=False, null=False)

    instructors     = models.ManyToManyField(
                            Profile,
                            related_name='courses_taught',
                            blank=True
                        )
    url             = models.URLField(null=True, blank=True)

    # status # Undefined, soon to start, in development, suspended, finished, aborted

    def __str__(self):
        return str(self.title)

class CoverItem(models.Model):
    item    = models.OneToOneField(Course, on_delete=models.CASCADE, null=False, blank=False)
    cover_image     = models.ImageField(upload_to='images', default='', blank=True, null=True)

class CoverCarrousel(models.Model):
    items = models.ManyToManyField(CoverItem, blank=True)

    def save(self, *args, **kwargs):
        if CoverCarrousel.objects.exists() and not self.pk:
        # if you'll not check for self.pk 
        # then error will also raised in update of exists model
            raise ValidationError('There is can be only one CoverCarrousel instance')
        return super(CoverCarrousel, self).save(*args, **kwargs)