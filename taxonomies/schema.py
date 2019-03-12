import graphene
import django_filters
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from category.models import Category, Tag

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class TagType(DjangoObjectType):
    class Meta:
        model = Tag