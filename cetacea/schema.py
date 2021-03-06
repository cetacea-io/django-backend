import graphene
import graphql_jwt
import graphql_social_auth

import users.schema
import organizations.schema
import projects.schema
import courses.schema
import accounts.schema
import recommender.schema
import searcher.schema
import taxonomies.schema
import shopping.schema

class Query(users.schema.Query,
            organizations.schema.Query,
            projects.schema.Query,
            courses.schema.Query,
            accounts.schema.Query,
            recommender.schema.Query,
            searcher.schema.Query,
            taxonomies.schema.Query,
            graphene.ObjectType):
    pass

class Mutation(
    accounts.schema.Mutation,
    users.schema.Mutation,
    projects.schema.Mutation,
    shopping.schema.Mutation,
    graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    social_auth = graphql_social_auth.SocialAuthJWT.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)