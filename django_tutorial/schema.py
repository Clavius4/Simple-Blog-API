# django_tutorial/schema.py
import graphene
from authors.schema import Query as AuthorsQuery, Mutation as AuthorsMutation
from categories.schema import Query as CategoriesQuery, Mutation as CategoriesMutation

class Query(AuthorsQuery, CategoriesQuery, graphene.ObjectType):
    pass

class Mutation(AuthorsMutation, CategoriesMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)