from django.db import models


class Course(models.Model):
    title           = models.CharField(max_length=60, blank=True, null=True)
    area            = models.CharField(max_length=60, blank=True, null=True)
    category        = models.CharField(max_length=60, blank=True, null=True)
    # cover_image     = models.ImageField(upload_to='images', blank=True, null=True)
    cover_image     = models.URLField()
    creator_image   = models.URLField()
    url             = models.URLField()

    quick_desc      = models.CharField(max_length=255, blank=True, null=True)
    overview        = models.TextField(blank=True, null=True)
    # Dates and stuff
    creation_date   = models.DateTimeField(blank=True, null=True) # when the project was created in cetacea
    due_date        = models.DateTimeField(blank=True, null=True) # When the project should be done
    start_date      = models.DateTimeField(blank=True, null=True) # If the project will start in a specific date

    location        = models.CharField(max_length=50, blank=True, null=True)

    #Wheter the project is published or still in creation process
    published       = models.BooleanField(default=False)

    # tags            = models.ManyToManyField(
    #                     Tag,
    #                     related_name='projects_related'
    #                 )
    # prefered_language

    # status # Undefined, soon to start, in development, suspended, finished, aborted

    # feed # Feed of what has been done timeline

    def __str__(self):
        return str(self.title)