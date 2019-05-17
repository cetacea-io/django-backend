import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Profile
from category.models import Category
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

class UpdateInterests(graphene.Mutation):
    user = graphene.String()

    class Arguments:
        categories = graphene.List(graphene.ID, required=True)
    
    def mutate(self, info, categories):
        if not info.context.user.is_authenticated:
            raise Exception("User not authenticated")
        else:
            profile = info.context.user.profile
            for category_id in categories:
                c = Category.objects.get(id=category_id)
                profile.interests.add(c)
            print(categories)
            user = 'momo'
            return UpdateInterests(user=user)

class Mutation(graphene.ObjectType):
    update_interests = UpdateInterests.Field()


class Query(graphene.ObjectType):
    profile = graphene.Field(ProfileType,
                            user=graphene.Int())

    def resolve_profile(self, info, **kwargs):
        user = kwargs.get('user')

        if user is not None:
            return Profile.objects.get(user=user)