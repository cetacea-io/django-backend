import factory
from . import models

from organizations.factories import OrganizationFactory

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'category.Category'

    title   = factory.Faker('word', ext_word_list=None)
    slug    = factory.LazyAttribute(lambda obj: '%s'.lower() % obj.title)

class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'category.Tag'

    title = factory.Faker('word', ext_word_list=None)