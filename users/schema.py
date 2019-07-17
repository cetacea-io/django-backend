from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType

import urllib.parse
import requests
from cetacea.settings.base import env

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

class GetAccessToken(graphene.Mutation):
    access_token = graphene.String()

    class Arguments:
        provider = graphene.String(required=True)
        code = graphene.String(required=True)
        redirect_uri = graphene.String(required=True)
    
    def mutate(self, info, provider, code, redirect_uri):
        FACEBOOK_ID = env('FACEBOOK_APP_ID', default='')
        FACEBOOK_SECRET = env('FACEBOOK_APP_SECRET', default='')

        params = {
            'client_id': FACEBOOK_ID,
            'client_secret': FACEBOOK_SECRET,
            'redirect_uri': redirect_uri,
            'code': code
        }
        url = 'https://graph.facebook.com/v3.3/oauth/access_token?' + urllib.parse.urlencode(params)

        resp = requests.get(url)

        print(resp.json()['access_token'])
        return GetAccessToken(access_token = resp.json()['access_token'])
        

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    get_access_token = GetAccessToken.Field()


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