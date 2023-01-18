"""Modelos de la aplicación Medidores."""
# Django
from django.db import models
from django.core.validators import MinValueValidator, RegexValidator

alphanumeric = RegexValidator(
    r'^[0-9a-zA-Z]*$', 
    'Only alphanumeric characters are allowed.'
)


class Medidor(models.Model):
    """ Modelo que representa un medidor."""
    id_key = models.CharField(
        primary_key=True,
        unique=True,
        max_length=10,
        validators=[alphanumeric])
    nombre = models.CharField(
        max_length=20,
        blank=False,
        null=False,
    )


class Medicion(models.Model):
    """ Modelo que representa la medición registrada en kwh de un medidor."""
    medidor = models.ForeignKey(
        Medidor,
        blank=False,
        null=False,
        on_delete=models.PROTECT,
        related_name='mediciones'
    )
    fecha_hora = models.DateTimeField(auto_now_add=True)
    consumo = models.DecimalField(
        validators=[MinValueValidator(0)],
        max_digits=12,
        decimal_places=2
    ) 
