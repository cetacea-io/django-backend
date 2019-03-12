import factory
from django.db.models.signals import post_save
from . import models

@factory.django.mute_signals(post_save)
class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Profile
    
    bio             = factory.Faker('text', max_nb_chars=200, ext_word_list=None)
    profile_picture = factory.django.ImageField(width=512, height=384)

    user            = factory.SubFactory('app.factories.UserFactory', profile=None)