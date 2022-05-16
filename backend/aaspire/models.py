from django.db import models

# Create your models here.
class Questions(models.Model):
    question = models.TextField()
    question_type = models.IntegerField()