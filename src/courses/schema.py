import graphene
import django_filters
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Course, Location

from organizations.schema import OrganizationType

# class CourseFilter(django_filters.FilterSet):
#     class Meta:
#         model = Course
#         fields = ['id', 'title', 'area']

# class CourseNode(DjangoObjectType):
#     class Meta:
#         model = Course
#         interfaces = (graphene.relay.Node, )

class CourseType(DjangoObjectType):
    class Meta:
        model = Course

class LocationType(DjangoObjectType):
    class Meta:
        model = Location

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


# class Query(graphene.ObjectType):
#     course = graphene.relay.Node.Field(CourseNode)
#     courses = DjangoFilterConnectionField(CourseNode, filterset_class=CourseFilter)