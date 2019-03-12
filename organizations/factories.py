import factory
from . import models

class OrganizationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Organization

    title           = factory.Faker('company')
    profile_picture = factory.django.ImageField(width=512, height=384)