import factory
from django.db.models.signals import post_save
from . import models

from accounts.factories import ProfileFactory

@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User
    
    username     = factory.Faker('user_name')
    first_name   = factory.Faker('first_name', locale='es_MX')
    last_name    = factory.Faker('last_name', locale='es_MX')
    email        = factory.LazyAttribute(lambda obj: '%s@%s.com' % (obj.first_name, obj.last_name))
    password     = factory.PostGenerationMethodCall('set_password', '1234')
    is_staff     = False
    is_superuser = False

    profile = factory.RelatedFactory(ProfileFactory, 'user')