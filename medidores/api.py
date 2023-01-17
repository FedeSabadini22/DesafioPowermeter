""" API Viewsets de la aplicación medidores."""
# Third Party
from rest_framework import viewsets, permissions

# Project
from .models import Medidor, Medicion
from .serializers import MedidorSerializer ,MedicionSerializer

class MedidorViewSet(viewsets.ModelViewSet):
    queryset = Medidor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MedidorSerializer


class MedicionViewSet(viewsets.ModelViewSet):
    queryset = Medicion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MedicionSerializer