import factory
from . import models

from organizations.factories import OrganizationFactory

class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Location

    text      = factory.Faker('address')
    latitude  = factory.Faker('latitude')
    longitude = factory.Faker('longitude')


class CourseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Course

    title       = factory.Faker('sentence', nb_words=5, variable_nb_words=True, ext_word_list=None)
    cover_image = factory.django.ImageField(width=1024, height=768)
    author      = factory.SubFactory(OrganizationFactory)
    quick_desc  = factory.Faker('text', max_nb_chars=200, ext_word_list=None)

    published   = True

    location    = factory.SubFactory(LocationFactory)

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            # Simply build, do nothing
            return
        if extracted:
            # A list of groups were passed in, use them
            for category in extracted:
                self.categories.add(category)

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            # Simply build, do nothing
            return
        if extracted:
            # A list of groups were passed in, use them
            for tag in extracted:
                self.tags.add(tag)
