import graphene
from graphene_django import DjangoObjectType
from .models import Questions

class QuestionsType(DjangoObjectType):
    class Meta:
        model = Questions
        fields = ("id", "question", "question_type")

class Query(graphene.ObjectType):
    all_questions = graphene.List(QuestionsType)

schema = graphene.Schema(query=Query)