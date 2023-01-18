""" API Viewsets de la aplicación medidores."""
# Third Party
from rest_framework import permissions, viewsets
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin
)
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.views import APIView

# Django
from django.http import Http404
from django.db.models import Max, Sum, Min, Avg

# Project
from .models import Medidor, Medicion
from .serializers import *


class MedidorListViewSet(viewsets.ModelViewSet):

    queryset = Medidor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MedidorSerializer


class MedidorCreateViewSet(GenericViewSet, CreateModelMixin):

      permission_classes = [permissions.AllowAny]
      serializer_class = MedidorSerializer


class MedicionListViewSet(GenericViewSet, ListModelMixin):

    queryset = Medicion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MedicionSerializer


class MedicionCreateViewSet(GenericViewSet, CreateModelMixin):

    permission_classes = [permissions.AllowAny]
    serializer_class = MedicionSerializer


class ConsumoMaximo(APIView):
    """
    API Endpoint que retorna el consumo de energía máximo registrado de un
    medidor.
    """

    def get_object(self, id):
        try:
            return Medidor.objects.get(id_key=id)
        except Medidor.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        medidor = self.get_object(id)
        consumo_maximo = Medicion.objects.filter(
            medidor=medidor.id_key).aggregate(Max('consumo')
        ).values()
        return Response (
            {f'Consumo Máximo del medidor {medidor.id_key}': consumo_maximo}
        )

    
class ConsumoMinimo(APIView):
    """
    API Endpoint que retorna el consumo de energía mínimo registrado de un
    medidor.
    """

    def get_object(self, id):
        try:
            return Medidor.objects.get(id_key=id)
        except Medidor.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        medidor = self.get_object(id)
        consumo_minimo = Medicion.objects.filter(
            medidor=medidor.id_key).aggregate(Min('consumo')
        ).values()
        return Response (
            {f'Consumo Mínimo del medidor {medidor.id_key}': consumo_minimo}
        )


class ConsumoTotal(APIView):
    """
    API Endpoint que retorna el consumo de energía total registrado de un
    medidor.
    """

    def get_object(self, id):
        try:
            return Medidor.objects.get(id_key=id)
        except Medidor.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        medidor = self.get_object(id)
        total = Medicion.objects.filter(
            medidor=medidor.id_key).aggregate(Sum('consumo')
        ).values()
        return Response ({f'Consumo Total del medidor {medidor.id_key}': total})


class ConsumoPromedio(APIView):
    """
    API Endpoint que retorna el consumo de energía promedio registrado de un
    medidor.
    """

    def get_object(self, id):
        try:
            return Medidor.objects.get(id_key=id)
        except Medidor.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        medidor = self.get_object(id)
        consumo_promedio = Medicion.objects.filter(
            medidor=medidor.id_key).aggregate(Avg('consumo')
        ).values()
        return Response (
            {f'Consumo Promedio del medidor {medidor.id_key}': consumo_promedio}
        )

