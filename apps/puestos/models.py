from apps.empleados.models import Empleado
from django.db import models

# Create your models here.
class Puesto(models.Model):
	"""docstring for Puesto"""
	id_puesto =models.CharField(max_length=50, primary_key=True)
	id_pk_empleado = models.ForeignKey(Empleado, null=False, blank=False, on_delete=models.CASCADE)
	puesto = models.CharField(max_length=20)
	estado = models.BooleanField(null=True)