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