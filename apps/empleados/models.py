from django.db import models

from apps.puestos.models import Puesto


class Empleado(models.Model):
	num_empleado = models.CharField("Número de Empleado", max_length=50, primary_key=True)
	puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)
	nombre = models.CharField("Nombre", max_length=50)
	apellido_paterno = models.CharField("Apellido Paterno", max_length=50)
	apellido_materno = models.CharField("Apellido Materno", max_length=50)
	calle = models.CharField("Calle", max_length=50)
	colonia = models.CharField("Colonia", max_length=50)
	delegacion = models.CharField("Delegación", max_length=50)
	municipio = models.CharField("Municipio", max_length=50)
	codigo_postal = models.CharField("Código Postal", max_length=50)

	class Meta:
		ordering = ['num_empleado']

	def __str__(self):
		return f"{self.num_empleado} - {self.nombre} {self.apellido_paterno} {self.apellido_materno}"
