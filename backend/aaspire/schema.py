import graphene
from graphene_django import DjangoObjectType

from .models import Questions


class QuestionsType(DjangoObjectType):
    class Meta:
        model = Questions
        fields = ("id", "question", "question_type")


class Query(graphene.ObjectType):
    all_questions = graphene.List(QuestionsType)

    def resolve_all_questions(root, info):
        return Questions.objects.all()


schema = graphene.Schema(query=Query)
