from django.db import models

# Create your models here.
class Empleado(models.Model):
	"""docstring for Empleado"""
	id_empleado = models.CharField(max_length=50, primary_key=True)
	nombre_usuario = models.CharField(max_length=50)
	apellido_pat = models.CharField(max_length=50)
	apellido_mat = models.CharField(max_length=50)
	calle = models.CharField(max_length=50)
	colonia = models.CharField(max_length=50)
	delegacion = models.CharField(max_length=50)
	municipio = models.CharField(max_length=50)
	codpost = models.CharField(max_length=50)
	id_puesto = models.ForeignKey(Puesto_empleado, null=False, blank=False, on_delete=models.CASCADE)

class Puesto_empleado(models.Model):
	"""docstring for Puesto_empleado"""
	id_puesto = models.CharField(max_length=50, primary_key=True)
	nombre_puesto = models.CharField(max_length=50)
	tipo_contrato = models.CharField(max_length=50)