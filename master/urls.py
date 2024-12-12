from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


urlpatterns = [
    path("create_base_variant", views.CreateBaseVariantView.as_view())
]
