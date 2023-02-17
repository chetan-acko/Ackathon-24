from django.urls import path
from . import views


urlpatterns = [
    path('questions/', views.UserQuestion),
    path('choices/', views.UserList),
    path('users/', views.QuestionChoice),
    path('responses/', views.UserResponse),
    path('qn/<int:question_id>', views.SurveyResult),
]