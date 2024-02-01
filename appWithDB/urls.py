from django.urls import path
from . import views

appwithdb_patterns = [
    path("version", views.apiVersion, name="apiVersion"),
    path("categories", views.CatAPIView.as_view()),
    path("coatings", views.CoatingAPIView.as_view()),
]