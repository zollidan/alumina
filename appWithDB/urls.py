from django.urls import path
from . import views

appwithdb_patterns = [
    path("", views.hello, name="welcomePage"),
    path("categories", views.CatAPIView.as_view()),
    path("coatings", views.CoatingAPIView.as_view()),
]