from apps.usuarios_departamento.models import Usuario_Departamento
from django.db import models

# Create your models here.
class Instalacion(models.Model):
	"""docstring for Compras"""
	id_instalacion = models.CharField(max_length=50, primary_key=True)
	colonia = models.CharField(max_length=50)
	codigo_postal = models.CharField(max_length=50)
	numero_piso = models.CharField(max_length=50)
	numero_instal = models.CharField(max_length=50)
	fecha_instal = models.DateTimeField(max_digits=5)
	rfc = models.ForeignKey(Usuario_Departamento, null=False, blank=False, on_delete=models.CASCADE)

	"""Posible tabla de lista de materiales"""
	class Material_instalacion(object):
		"""docstring for Material_instalacion"""
		id_instalacion = models.ForeignKey(Instalacíon, null=False, blank=False, on_delete=models.CASCADE)
		cantidad = models.IntegerField()
			