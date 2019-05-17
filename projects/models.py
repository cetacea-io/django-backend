from django.db import models
from django.contrib.auth import get_user_model

from accounts.models import Profile
from organizations.models import Organization

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


# Create your models here.
class Project(models.Model):
    # published_by_user = models.ForeignKey(get_user_model(), related_name='projects', on_delete=models.CASCADE)
    # published_by_organization = models.ForeignKey(Organization, related_name='projects', on_delete=models.CASCADE)
    author          = models.ForeignKey(Profile, related_name="projects_created", on_delete=models.SET_NULL, null=True)
    title           = models.CharField(max_length=60, blank=True, null=True)
    category        = models.CharField(max_length=60, blank=True, null=True)
    cover_image     = models.ImageField(upload_to='images', null=True)
    likes           = models.ManyToManyField(
                        get_user_model(),
                        related_name='projects_liked',
                        blank=True,
                    )
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

    comments        = models.ManyToManyField(
                        Comment,
                        related_name='project',
                        blank=True
                    )

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