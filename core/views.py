from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Question, Choice, User, Responses
from .serializers import QuestionSerializer, ChoiceSerializer, UserSerializer, ResponseSerializer
from django.http import JsonResponse


@api_view(['GET', 'POST'])
def UserQuestion(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def QuestionChoice(request):
    if request.method == 'GET':
        choices = Choice.objects.all()
        serializer = ChoiceSerializer(choices, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ChoiceSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def UserList(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def UserResponse(request):
    user = User.objects.get(pk=request.data['user'])
    responses = request.data['responses']
    for res in responses:
        choice = Choice.objects.get(pk=res['choice'])
        response = Responses.objects.create(user=user, choice=choice)
        response.save()
    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def SurveyResult(request, question_id):
    choices = Choice.objects.filter(question_id=question_id).annotate(response_count=Count('responses'))
    data = [{'choice_id': choice.id, 'response_count': choice.response_count} for choice in choices]
    return JsonResponse({'items': data})
