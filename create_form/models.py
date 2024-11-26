from django.db import models
from django.contrib.auth.models import User

class Choices(models.Model):
    choice = models.CharField(max_length=5000)
    is_answer = models.BooleanField(default=False)

class Questions(models.Model):
    question = models.CharField(max_length= 10000)
    question_type = models.CharField(max_length=20)
    required = models.BooleanField(default= False)
    answer_key = models.CharField(max_length = 5000, blank = True)
    choices = models.ManyToManyField(Choices, related_name = "choices")

class Form(models.Model):
    code = models.CharField(max_length=30)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=10000, blank = True)
    creator = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "creator")
    collect_email = models.BooleanField(default=False)
    authenticated_responder = models.BooleanField(default = False)
    edit_after_submit = models.BooleanField(default=False)
    confirmation_message = models.CharField(max_length = 10000, default = "Your response has been recorded.")
    createdAt = models.DateTimeField(auto_now_add = True)
    updatedAt = models.DateTimeField(auto_now = True)
    questions = models.ManyToManyField(Questions, related_name = "questions")