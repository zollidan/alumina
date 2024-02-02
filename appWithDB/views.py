from django.shortcuts import HttpResponse
from .models import *
from rest_framework import generics
from .serializer import *

class CatAPIView(generics.ListAPIView):
   queryset = categories.objects.all()
   serializer_class = CatsSerializer

class CoatingAPIView(generics.ListAPIView):
   queryset = coatings.objects.all()
   serializer_class = CoatingSerializer

class OrdersAPIView(generics.ListAPIView):
   queryset = orders.objects.all()
   serializer_class = OrdersSerializer

class PanelSizeAPIView(generics.ListAPIView):
   queryset = panel_size.objects.all()
   serializer_class = PanelSizeSerializer

class PanelThicknessAPIView(generics.ListAPIView):
   queryset = panel_thickness.objects.all()
   serializer_class = PanelThicknessSerializer

class LayerThicknessAPIView(generics.ListAPIView):
   queryset = layer_thickness.objects.all()
   serializer_class = LayerThicknessSerializer
    

def apiVersion(request):
    return HttpResponse("LeFort Tech Inc. v1.0")
