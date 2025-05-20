from django.test import TestCase

# Create your tests here.
from rest_framework import serializers
from .models import Almacen

class AlmacenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Almacen
        fields = ['id','nombre','ubicacion']