"""Paths de la app medidores."""
# Third Party
from rest_framework import routers
# Django
from django.urls import path, include
# Project
from .api import *

router = routers.DefaultRouter()

router.register('alta_medidor', MedidorCreateViewSet, 'alta_medidor')
router.register('registrar_medicion', MedicionCreateViewSet, 'registrar_medicion')
router.register('medidores', MedidorListViewSet, 'medidores')
router.register('mediciones', MedicionListViewSet, 'mediciones')

urlpatterns = []
urlpatterns.extend([
    path('api/', include(router.urls)),
])