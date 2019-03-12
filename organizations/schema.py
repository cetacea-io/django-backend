import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Organization


class OrganizationType(DjangoObjectType):
    class Meta:
        model = Organization

    def resolve_profile_picture(self, *_):
        if self.profile_picture:
            return self.profile_picture.url
        else:
            return ""

class Query(graphene.ObjectType):
    organization = graphene.Field(OrganizationType,
                            id=graphene.Int())

    organizations = graphene.List(OrganizationType)

    def resolve_organization(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Organization.objects.get(id=id)


    def resolve_organizations(self, info, **kwargs):
        return Organization.objects.filter(published=True)
