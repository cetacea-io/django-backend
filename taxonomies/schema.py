import graphene
import django_filters
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from category.models import Category, Tag
from .models import MainCategory

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class TagType(DjangoObjectType):
    class Meta:
        model = Tag

class MainCategoryType(DjangoObjectType):
    title = graphene.String()
    id = graphene.Int()

    class Meta:
        model = MainCategory

    def resolve_thumbnail(self, *_):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            return ""

    def resolve_title(self, *_):
        return self.category.title

    def resolve_id(self, *_):
        return self.category.id

class Query(graphene.ObjectType):
    main_categories = graphene.List(MainCategoryType)

    def resolve_main_categories(self, info, **kwargs):
        return MainCategory.objects.all()