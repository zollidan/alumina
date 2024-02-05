from django.urls import path
from . import views


appwithdb_patterns = [
    path("version", views.apiVersion, name="apiVersion"),
    path("categories", views.CatAPIView.as_view()),
    path("coatings", views.CoatingAPIView.as_view()),
    path("orders", views.OrdersAPIView.as_view()),
    path("create-order", views.CreateOrderAPIView.as_view()),
    path("panelsize", views.PanelSizeAPIView.as_view()),
    path("panelthickness", views.PanelThicknessAPIView.as_view()),
    path("layerthickness", views.LayerThicknessAPIView.as_view()),
    
]