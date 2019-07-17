import graphene
import django_filters
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Course, CourseClassification, CoverItem
from events.models import Location, DateAndTime

from organizations.schema import OrganizationType
from taxonomies.schema import CategoryType, TagType
from projects.schema import Common

from recommender.functionality import recommend_courses_by_course

# class CourseFilter(django_filters.FilterSet):
#     class Meta:
#         model = Course
#         fields = ['id', 'title', 'area']

# class CourseNode(DjangoObjectType):
#     class Meta:
#         model = Course
#         interfaces = (graphene.relay.Node, )
class LocationType(DjangoObjectType):
    class Meta:
        model = Location

class DateAndTimeType(DjangoObjectType):
    class Meta:
        model = DateAndTime

class CourseClassificationType(DjangoObjectType):
    class Meta:
        model = CourseClassification


class CoverItemType(graphene.ObjectType):
    id = graphene.Int()
    title = graphene.String()
    author = graphene.String()
    image = graphene.String()
    classification = graphene.String()
    area = graphene.String()

    def resolve_id(self, *_):
        return self.item.id

    def resolve_title(self, *_):
        return self.item.title

    def resolve_author(self, *_):
        return self.item.author

    def resolve_image(self, *_):
        if self.cover_image:
            return self.cover_image.url
        else:
            return ""
        
    def resolve_classification(self, *_):
        return self.item.classification.title

    def resolve_area(self, *_):
        return self.item.area


class CourseType(DjangoObjectType):
    recommended = graphene.List(lambda: CourseType, args={'total_recommended': graphene.Int()})
    gallery     = graphene.List(graphene.String)

    class Meta:
        model = Course
        interfaces = (Common, )

    def resolve_cover_image(self, *_):
        if self.cover_image:
            return self.cover_image.url
        else:
            return ""

    def resolve_recommended(self, *_, total_recommended):
        return recommend_courses_by_course(total_recommended)

    def resolve_gallery(self, *_):
        from events.models import Picture
        pics = Picture.objects.all()[:5]
        # pics = self.pictures.all()[:5]
        new = []
        for pic in pics:
            new.append(pic.content.url)
        return new


class Query(graphene.ObjectType):
    course = graphene.Field(CourseType,
                            id=graphene.Int())

    courses = graphene.List(CourseType,
                            category=graphene.Int())

    cover = graphene.Field(CoverItemType)

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

    def resolve_cover(self, info, **kwargs):
        return CoverItem.objects.get(id=1)


# class Query(graphene.ObjectType):
#     course = graphene.relay.Node.Field(CourseNode)
#     courses = DjangoFilterConnectionField(CourseNode, filterset_class=CourseFilter)