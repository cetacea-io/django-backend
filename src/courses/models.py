from django.db import models

from accounts.models import Profile

class Location(models.Model):
    text = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.text


class Course(models.Model):
    title           = models.CharField(max_length=60, blank=True, null=True)
    author          = models.ForeignKey('organizations.Organization', on_delete=models.SET_NULL, null=True, blank=True)
    area            = models.CharField(max_length=60, blank=True, null=True)
    category        = models.CharField(max_length=60, blank=True, null=True)
    # cover_image     = models.ImageField(upload_to='images', blank=True, null=True)
    cover_image     = models.URLField()

    quick_desc      = models.CharField(max_length=255, blank=True, null=True)
    overview        = models.TextField(blank=True, null=True)
    # Dates and stuff
    creation_date   = models.DateTimeField(blank=True, null=True) # when the project was created in cetacea
    due_date        = models.DateTimeField(blank=True, null=True) # When the project should be done
    start_date      = models.DateTimeField(blank=True, null=True) # If the project will start in a specific date

    location        = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)

    #Wheter the project is published or still in creation process
    published       = models.BooleanField(default=False)

    instructors     = models.ManyToManyField(
                        Profile,
                        related_name='courses_taught',
                        blank=True
                    )

    # tags            = models.ManyToManyField(
    #                     Tag,
    #                     related_name='projects_related'
    #                 )
    # prefered_language

    # status # Undefined, soon to start, in development, suspended, finished, aborted

    # feed # Feed of what has been done timeline

    def __str__(self):
        return str(self.title)