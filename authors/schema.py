# authors/schema.py
import graphene
from graphene_django.types import DjangoObjectType
from .models import Author

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ('id', 'name', 'bio', 'created_at', 'updated_at')

class Query(graphene.ObjectType):
    all_authors = graphene.List(AuthorType)
    author = graphene.Field(AuthorType, id=graphene.Int())

    def resolve_all_authors(self, info, **kwargs):
        return Author.objects.all()

    def resolve_author(self, info, id):
        return Author.objects.get(pk=id)

class CreateAuthor(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        bio = graphene.String()

    author = graphene.Field(AuthorType)

    def mutate(self, info, name, bio):
        author = Author(name=name, bio=bio)
        author.save()
        return CreateAuthor(author=author)

class UpdateAuthor(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        name = graphene.String()
        bio = graphene.String()

    author = graphene.Field(AuthorType)

    def mutate(self, info, id, name=None, bio=None):
        author = Author.objects.get(pk=id)
        if name:
            author.name = name
        if bio:
            author.bio = bio
        author.save()
        return UpdateAuthor(author=author)

class DeleteAuthor(graphene.Mutation):
    class Arguments:
        id = graphene.Int()

    success = graphene.Boolean()

    def mutate(self, info, id):
        author = Author.objects.get(pk=id)
        author.delete()
        return DeleteAuthor(success=True)

class Mutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()
    update_author = UpdateAuthor.Field()
    delete_author = DeleteAuthor.Field()