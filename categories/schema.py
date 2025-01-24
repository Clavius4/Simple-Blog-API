# categories/schema.py
import graphene
from graphene_django.types import DjangoObjectType
from .models import Category

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')

class Query(graphene.ObjectType):
    all_categories = graphene.List(CategoryType)
    category = graphene.Field(CategoryType, id=graphene.Int())

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_category(self, info, id):
        return Category.objects.get(pk=id)

class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        description = graphene.String()

    category = graphene.Field(CategoryType)

    def mutate(self, info, name, description):
        category = Category(name=name, description=description)
        category.save()
        return CreateCategory(category=category)

class UpdateCategory(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        name = graphene.String()
        description = graphene.String()

    category = graphene.Field(CategoryType)

    def mutate(self, info, id, name=None, description=None):
        category = Category.objects.get(pk=id)
        if name:
            category.name = name
        if description:
            category.description = description
        category.save()
        return UpdateCategory(category=category)

class DeleteCategory(graphene.Mutation):
    class Arguments:
        id = graphene.Int()

    success = graphene.Boolean()

    def mutate(self, info, id):
        category = Category.objects.get(pk=id)
        category.delete()
        return DeleteCategory(success=True)

class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()