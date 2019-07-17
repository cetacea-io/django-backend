import graphene
from graphene import relay
import django_filters
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from courses.models import Course
from category.models import Category
from projects.models import Project

from courses.schema import CourseType
from projects.schema import ProjectType
from taxonomies.schema import CategoryType, TagType
from recommender.schema import CarrouselConnection, Carrousel

# class Item(relay.Node):
#     class Meta:
#         name = 'Item'
    
#     @staticmethod
#     def to_global_id(type, id):
#         return '{}:{}'.format(type, id)
    
#     @staticmethod
#     def get_node_from_global_id(info, global_id, only_type=None):
#         type, id = global_id.split(':')

#         if only_type:
#             assert type == only_type._meta.name, 'Received not compatible node.'
        
#         if type == 'CourseType':
#             print('course')
#             return CourseType
#         elif type == 'ProjectType':
#             print('project')
#             return ProjectType

# class ItemConnection(relay.Connection):
#     class Meta:
#         node = Item

# class CourseNode(CourseType):
#     class Meta:
#         model = Course
#         interfaces = (relay.Node, )

# class ProjectNode(ProjectType):
#     class Meta:
#         model = Project
#         interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    search = relay.ConnectionField(CarrouselConnection, query=graphene.String())


    def resolve_search(self, info, **kwargs):
        query = kwargs.get('query')

        # if iteration == 1:
        # if info.context.user.is_authenticated():
            # pass
        # else:
        all = []

        item1 = Carrousel (
            title       = 'Proyectos destacados',
            description = 'Proyectos en los que puedes colaborar',
            content     = Course.objects.filter(title__icontains=query)
        )

        all.append(item1)

        return all