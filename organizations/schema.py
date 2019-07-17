import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Organization

from django.contrib.auth import get_user_model
from users.schema import UserType


class OrganizationType(DjangoObjectType):
    class Meta:
        model = Organization

    def resolve_profile_picture(self, *_):
        if self.profile_picture:
            return self.profile_picture.url
        else:
            return ""

class OrganizationUserUnion(graphene.types.Union):
    class Meta:
        types = [OrganizationType, UserType]

class Query(graphene.ObjectType):
    account = graphene.Field(OrganizationUserUnion, username=graphene.String())

    organization = graphene.Field(OrganizationType,
                            id=graphene.Int())

    organizations = graphene.List(OrganizationType)

    def resolve_account(self, info, **kwargs):
        username = kwargs.get('username')

        if username is not None:
            account = None
            try:
                account = Organization.objects.get(username=username)
            except Organization.DoesNotExist:
                try:
                    account = get_user_model().objects.get(username=username)
                except get_user_model().DoesNotExist:
                    return None
                    
            return account


    def resolve_organization(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Organization.objects.get(id=id)


    def resolve_organizations(self, info, **kwargs):
        return Organization.objects.filter(published=True)
