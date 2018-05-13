from apps.puestos.models import Puesto
from django.db import models

# Create your models here.
class Empleado(models.Model):
	"""docstring for Empleado"""
	id_empleado = models.CharField(max_length=50, primary_key=True)
	id_pk_puesto =models.ForeignKey(Puesto, null=False, blank=False, on_delete=models.CASCADE)
	nombre_usuario = models.CharField(max_length=50)
	apellido_pat = models.CharField(max_length=50)
	apellido_mat = models.CharField(max_length=50)
	calle = models.CharField(max_length=50)
	colonia = models.CharField(max_length=50)
	delegacion = models.CharField(max_length=50)
	municipio = models.CharField(max_length=50)
	codpost = models.CharField(max_length=50)

