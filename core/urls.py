from django.urls import path
from . import views


urlpatterns = [
    path('questions/', views.UserQuestion),
    path('users/', views.UserList),
    path('choices/', views.QuestionChoice),
    path('responses/', views.UserResponse),
    path('qn/<int:question_id>', views.SurveyResult),
]
