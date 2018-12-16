import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Course


class CourseType(DjangoObjectType):
    class Meta:
        model = Course

class Query(graphene.ObjectType):
    course = graphene.Field(CourseType,
                            id=graphene.Int())

    courses = graphene.List(CourseType,
                            area=graphene.String())

    def resolve_course(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Course.objects.get(id=id)


    def resolve_courses(self, info, **kwargs):
        area = kwargs.get('area')

        if area is not None:
            return Course.objects.filter(published=True, area=area)
        else:
            return Course.objects.filter(published=True)