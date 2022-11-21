from django.urls import path
from .views import PhotoDetail

urlpatterns = [
    path("phoths/<int:pk>", PhotoDetail.as_view()),
]
