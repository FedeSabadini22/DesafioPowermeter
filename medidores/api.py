""" API Viewsets de la aplicación medidores."""
# Third Party
from rest_framework import permissions
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin
)
from rest_framework.viewsets import GenericViewSet

# Project
from .models import Medidor, Medicion
from .serializers import MedidorSerializer ,MedicionSerializer


class MedidorListViewSet(GenericViewSet, ListModelMixin):

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