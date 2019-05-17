import graphene
import django_filters
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Course, Location, DateAndTime, CourseClassification

from organizations.schema import OrganizationType
from taxonomies.schema import CategoryType, TagType

from recommender.functionality import recommend_courses_by_course

# class CourseFilter(django_filters.FilterSet):
#     class Meta:
#         model = Course
#         fields = ['id', 'title', 'area']

# class CourseNode(DjangoObjectType):
#     class Meta:
#         model = Course
#         interfaces = (graphene.relay.Node, )

class CourseType(DjangoObjectType):
    total_likes = graphene.Int()
    total_views = graphene.Int()
    recommended = graphene.List(lambda: CourseType, args={'total_recommended': graphene.Int()})

    class Meta:
        model = Course

    def resolve_cover_image(self, *_):
        if self.cover_image:
            return self.cover_image.url
        else:
            return ""
    
    def resolve_total_likes(self, *_):
        return 55454512
    
    def resolve_total_views(self, *_):
        return 1205423125

    def resolve_recommended(self, *_, total_recommended):
        return recommend_courses_by_course(total_recommended)

class LocationType(DjangoObjectType):
    class Meta:
        model = Location

class DateAndTimeType(DjangoObjectType):
    class Meta:
        model = DateAndTime

class CourseClassificationType(DjangoObjectType):
    class Meta:
        model = CourseClassification


class Query(graphene.ObjectType):
    course = graphene.Field(CourseType,
                            id=graphene.Int())

    courses = graphene.List(CourseType,
                            category=graphene.Int())

    def resolve_course(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Course.objects.get(id=id)


    def resolve_courses(self, info, **kwargs):
        category = kwargs.get('category')

        if category is not None:
            return Course.objects.filter(published=True, categories__id=category)
        else:
            return Course.objects.filter(published=True)


# class Query(graphene.ObjectType):
#     course = graphene.relay.Node.Field(CourseNode)
#     courses = DjangoFilterConnectionField(CourseNode, filterset_class=CourseFilter)