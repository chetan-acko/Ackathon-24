from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=100)


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    count = models.IntegerField(default=0)


class User(models.Model):
    name = models.CharField(max_length=50)


class Responses(models.Model):
    user = models.ForeignKey(User, related_name='responses', on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, related_name='responses', on_delete=models.CASCADE)

