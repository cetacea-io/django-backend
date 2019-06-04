import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Project, Comment, Position

from accounts.schema import ProfileType

class AuthorType(graphene.ObjectType):
    id = graphene.ID(required=True)
    title = graphene.String(required=True)
    picture = graphene.String(required=True)

    def resolve_id(self, info, *_):
        return self.id

    def resolve_title(self, info, *_):
        if self.__class__.__name__ == 'User':
            return '{} {}'.format(self.first_name, self.last_name)
        elif self.__class__.__name__ == 'Organization':
            return self.title

    def resolve_picture(self, info, *_):
        if self.__class__.__name__ == 'User':
            return self.profile.profile_picture.url
        elif self.__class__.__name__ == 'Organization':
            return self.profile_picture.url

class Common(graphene.Interface):
    author = graphene.Field(AuthorType)
    total_likes = graphene.Int()
    total_views = graphene.Int()

    def resolve_total_likes(self, *_):
        return 55454512

    def resolve_total_views(self, *_):
        return 1205423125

class ProjectType(DjangoObjectType):
    random_contributors = graphene.List(graphene.String)
    total_contributors = graphene.Int()
    
    class Meta:
        model = Project
        interfaces = (Common, )
        exclude_fields = ('published_by_user', 'published_by_organization')

    def resolve_cover_image(self, *_):
        if self.cover_image:
            return self.cover_image.url
        else:
            return ""
    
    def resolve_random_contributors(self, info, *_):
        contributors_list = []
        for position in self.positions.all():
            for applicant in position.applicants.all():
                contributors_list.append(applicant.profile.profile_picture.url)
        return contributors_list
        

    def resolve_total_contributors(self, *_):
        total_contributors = 0
        for position in self.positions.all():
            for applicant in position.applicants.all():
                total_contributors += 1
        return total_contributors

class PositionType(DjangoObjectType):
    already_applied = graphene.Boolean()
    contributors    = graphene.List(ProfileType)
    random_contributors = graphene.List(graphene.String)

    class Meta:
        model = Position

    def resolve_already_applied(self, info, *_):
        #If the user is authenticated and the user has already applied to the position
        if (info.context.user.is_authenticated) and (info.context.user in self.applicants.all()):
            return True
        return False
    
    def resolve_contributors(self, info, *_):
        contributors_list = []
        for contributor in self.applicants.all():
            contributors_list.append(contributor.profile)
        return contributors_list
    
    def resolve_random_contributors(self, info, *_):
        contributors_list = []
        for contributor in self.applicants.all():
            contributors_list.append(contributor.profile.profile_picture.url)
        return contributors_list



class CommentType(DjangoObjectType):
    name = graphene.String()
    class Meta:
        model = Comment

# class AuthorType(ObjectType):
#     name = graphene.String()
#     picture = graphene.String()

class Query(graphene.ObjectType):
    project = graphene.Field(ProjectType,
                            id=graphene.Int())

    projects = graphene.List(ProjectType)

    position = graphene

    # author = graphene.Field(AuthorType)

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

class JoinProject(graphene.Mutation):
    status = graphene.Boolean()
    position = graphene.Int()

    class Arguments:    
        position = graphene.Int()

    def mutate(self, info, position):
        if not info.context.user.is_authenticated:
            raise Exception("User is not authenticated")
        else:
            new_position = Position.objects.get(id=position)
            actual_applicant = info.context.user
            new_position.applicants.add(actual_applicant)
            print(actual_applicant)
            status = True

            return JoinProject(
                status = status
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
                author = info.context.user,
                # project = new_project,
                content = content
            )
            comment.save()
            new_project.comments.add(comment)

            return CreateComment(
                # author = info.context.user,
                # project_id = project_id,
                content = content
            )

class Mutation(graphene.ObjectType):
    create_comment = CreateComment.Field()
    create_project = CreateProject.Field()
    join_project = JoinProject.Field()