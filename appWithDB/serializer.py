from rest_framework import serializers
from .models import *

class CatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = categories
        fields = '__all__'

class CoatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = coatings
        fields = '__all__'

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = orders
        fields = '__all__'

class PanelSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = panel_size
        fields = '__all__'

class PanelThicknessSerializer(serializers.ModelSerializer):
    class Meta:
        model = panel_size
        fields = '__all__'

class LayerThicknessSerializer(serializers.ModelSerializer):
    class Meta:
        model = layer_thickness
        fields = '__all__'