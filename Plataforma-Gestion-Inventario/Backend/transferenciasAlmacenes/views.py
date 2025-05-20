from django.shortcuts import render
from rest_framework import serializers
from GestionMovimientos.models import Transferencia
from GestionProductos.serializers import ProductoSerializer
from GestionUsuarios.serializers import UsuarioSerializer
from .serializers import AlmacenSerializer
# Create your views here.

class TransferenciaSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    producto_id = serializers.PrimaryKeyRelatedField(
        queryset=Transferencia._meta.get_field('producto').related_model.objects.all(),
        source='producto',
        write_only = True
    )
    
    origen = AlmacenSerializer(read_only=True)
    origen_id = serializers.PrimaryKeyRelatedField(
        queryset=Transferencia._meta.get_field('origen').related_model.objects.all(),
        source='destino',
        write_only=True
    )
    usuario = UsuarioSerializer(read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(
        queryset=Transferencia._meta.get_field('usuario').related_model.objects.all(),
        source='usuario',
        write_only=True
    )
    
    class Meta:
        model = Transferencia
        fields = [
          'id','producto','producto_id',
          'cantidad',
          'origen','origen_id',
          'destino','destino_id',
          'usuario','usuario_id',
          'fecha'
        ]
        read_only_fields = ['fecha']
