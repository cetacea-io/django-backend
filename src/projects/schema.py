import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Project, Comment, Position


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project

class PositionType(DjangoObjectType):
    class Meta:
        model = Position

class CommentType(DjangoObjectType):
    class Meta:
        model = Comment

class Query(graphene.ObjectType):
    project = graphene.Field(ProjectType,
                            id=graphene.Int())

    projects = graphene.List(ProjectType)

    def resolve_project(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Project.objects.get(id=id)


    def resolve_projects(self, info, **kwargs):
        return Project.objects.filter(published=True)

class CreateProject(graphene.Mutation):
    category = graphene.String()
    quick_desc = graphene.String()

    class Arguments:
        category = graphene.String()
        quick_desc = graphene.String()

    def mutate(self, info, category, quick_desc):

        if not info.context.user.is_authenticated:
            raise Exception("User not authenticated")
        
        else:
            project = Project(category=category, quick_desc=quick_desc)
            project.save()

            return CreateProject(
                category = project.category,
                quick_desc = project.quick_desc,
            )

class CreateComment(graphene.Mutation):
    content = graphene.String()
    project = graphene.Int()

    class Arguments:
        content = graphene.String()
        project = graphene.Int()

    def mutate(self, info, content, project):

        if not info.context.user.is_authenticated:
            raise Exception("User not authenticated")

        else:
            new_project = Project.objects.get(id=project)
            comment = Comment(
                        owner = info.context.user,
                        # project = new_project,
                        content = content
                    )
            comment.save()
            new_project.comments.add(comment)

            return CreateComment(
                # owner = info.context.user,
                # project_id = project_id,
                content = content
            )

class Mutation(graphene.ObjectType):
    create_comment = CreateComment.Field()
    create_project = CreateProject.Field()