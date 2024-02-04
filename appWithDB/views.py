from django.shortcuts import HttpResponse
from django.http import JsonResponse
from .models import *
from rest_framework import generics
from rest_framework.response import Response
from .serializer import *

class CatAPIView(generics.ListAPIView):
   queryset = categories.objects.all()
   serializer_class = CatsSerializer
   def post(self, request):
      newCat = CatsSerializer(data=request.data)
      if newCat.is_valid():
         newCat.save()
      return Response(status=201)
   
   
class CoatingAPIView(generics.ListAPIView):
   queryset = coatings.objects.all()
   serializer_class = CoatingSerializer
   def post(self, request):
      newCoating = CoatingSerializer(data=request.data)
      if newCoating.is_valid():
         newCoating.save()
      return Response(status=201)

class OrdersAPIView(generics.ListAPIView):
   queryset = orders.objects.all()
   serializer_class = OrdersSerializer

class PanelSizeAPIView(generics.ListAPIView):
   queryset = panel_size.objects.all()
   serializer_class = PanelSizeSerializer
   def post(self, request):
      newPanelSize = PanelSizeSerializer(data=request.data)
      if newPanelSize.is_valid():
         newPanelSize.save()
      return Response(status=201)

class PanelThicknessAPIView(generics.ListAPIView):
   queryset = panel_thickness.objects.all()
   serializer_class = PanelThicknessSerializer
   def post(self, request):
      newPanelThickness = PanelThicknessSerializer(data=request.data)
      if newPanelThickness.is_valid():
         newPanelThickness.save()
      return Response(status=201)

class LayerThicknessAPIView(generics.ListAPIView):
   queryset = layer_thickness.objects.all()
   serializer_class = LayerThicknessSerializer
   def post(self, request):
      newLayerThickness = LayerThicknessSerializer(data=request.data)
      if newLayerThickness.is_valid():
         newLayerThickness.save()
      return Response(status=201)
    




def apiVersion(request):
    return JsonResponse({"trademark":"LeFort Tech Inc.", "version":"0.2"})
