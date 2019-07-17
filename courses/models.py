from django.db import models

from accounts.models import Profile

from events.models import CommonItem, Location, DateAndTime

class Cost(models.Model):
    pass


class CourseClassification(models.Model):
    # Curso, Taller, Diplomado
    title = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title


class Course(CommonItem):

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