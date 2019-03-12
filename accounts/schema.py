import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Profile
from taxonomies.schema import CategoryType, TagType


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        # exclude_fields = ('published_by_user', 'published_by_organization')

    def resolve_profile_picture(self, *_):
        if self.profile_picture:
            return self.profile_picture.url
        else:
            return ""

class Query(graphene.ObjectType):
    profile = graphene.Field(ProfileType,
                            user=graphene.Int())

    def resolve_profile(self, info, **kwargs):
        user = kwargs.get('user')

        if user is not None:
            return Profile.objects.get(user=user)