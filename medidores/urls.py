"""Paths de la app medidores."""

from rest_framework import routers
from .api import MedicionViewSet, MedidorViewSet

router = routers.DefaultRouter()

router.register('api/medidores', MedidorViewSet, 'medidores')
router.register('api/mediciones', MedicionViewSet, 'mediciones')

urlpatterns = router.urls