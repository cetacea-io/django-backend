from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType

from accounts.schema import ProfileType
from taxonomies.schema import CategoryType, TagType


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
    
    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username = username,
            email = email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


class Query(graphene.AbstractType):
    me = graphene.Field(UserType)
    user = graphene.Field(UserType, 
                        id=graphene.Int(), 
                        username=graphene.String())
    users = graphene.List(UserType)

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        username = kwargs.get('username')

        if id is not None:
            return get_user_model().objects.get(id=id)

        if username is not None:
            return get_user_model().objects.get(username=username)

    def resolve_users(self, info):
        return get_user_model().objects.all()

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged!')

        return user