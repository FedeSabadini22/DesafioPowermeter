""" Serializers de la aplicación medidores."""
# Third Party
from rest_framework import serializers

# Project
from .models import Medicion, Medidor


class MedidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medidor
        fields = ('id_key', 'nombre')


class MedicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicion
        fields = ('id', 'medidor', 'fecha_hora', 'consumo')