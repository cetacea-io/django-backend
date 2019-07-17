from django.db import models
from django.contrib.auth import get_user_model

from accounts.models import Profile
from organizations.models import Organization

from events.models import CommonItem, Comment

# class Group(models.Model):
#     name        = models.CharField(max_length=70)
#     category    = modele.
#     description = models.CharField(max_length=255)
#     members     = models.ManyToManyField(
#                     get_user_model(),
#                     related_name='groups'
#                 )

# class Collaborator(models.Model):
    

#     def __str__(self):
#         return str(self.title)

# Create your models here.
class Project(CommonItem):

    category        = models.CharField(max_length=60, blank=True, null=True)
    # Dates and stuff
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


class Position(models.Model):
    # locacion, si es necesario estar presente en la locacion
    # lenguaje preferido
    project         = models.ForeignKey(Project, related_name='positions', on_delete=models.CASCADE)
    title           = models.CharField(max_length=20, blank=False, null=False)
    description     = models.CharField(max_length=255, blank=False, null=False)
    time            = models.CharField(max_length=255, blank=False, null=False)
    compensation    = models.CharField(max_length=255, blank=False, null=False)
    requirements    = models.CharField(max_length=255, blank=False, null=False)
    applicants      = models.ManyToManyField(
                        get_user_model(),
                        related_name="positions_interested",
                        blank=True
                    )

    def __str__(self):
        return str(self.title)


# class Position(models.Model):
#     lugares abiertos # Numero de lugares que estan abiertos
#     usuarios dentro del team # Usuarios que ya estan trabajando en ese puesto
#     usuarios que hicieron request pero aun no son aceptados 