from django.db import models

from apps.usuarios_departamentos.models import UsuarioDepartamento
from apps.empleados.models import Empleado


class Instalacion(models.Model):
	id = models.CharField(max_length=50, primary_key=True)
	calle = models.CharField(max_length=50)
	colonia = models.CharField(max_length=50)
	codigo_postal = models.CharField(max_length=50)
	numero_piso = models.CharField(max_length=50)
	# numero_instalacion = models.CharField(max_length=50)
	fecha_instalacion = models.DateTimeField(auto_now=False, auto_now_add=False)
	usuario_departamento = models.ForeignKey(UsuarioDepartamento, null=False, blank=False, on_delete=models.CASCADE)
	empleados = models.ManyToManyField(Empleado)
