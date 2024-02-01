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
    

def apiVersion(request):
    return HttpResponse("LeFort Tech Inc. v1.0")
