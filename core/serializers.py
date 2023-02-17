from rest_framework import serializers
from .models import Question, Choice, User, Responses


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text']


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'text', 'question')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name')


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responses
        fields = ('id', 'user', 'choice')

