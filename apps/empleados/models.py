from django.db import models

# from apps.puestos.models import Puesto


PUESTOS = (
	('1', 'Puesto 1'),
	('2', 'Puesto 2'),
	('3', 'Puesto 3'),
)

class Empleado(models.Model):
<<<<<<< HEAD
	"""docstring for Empleado"""
	empleado = models.CharField(max_length=50, primary_key=True)
	puesto =models.ForeignKey(Puesto, null=False, blank=False, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=50)
	apellido_pat = models.CharField(max_length=50)
	apellido_mat = models.CharField(max_length=50)
	calle = models.CharField(max_length=50)
	colonia = models.CharField(max_length=50)
	delegacion = models.CharField(max_length=50)
	municipio = models.CharField(max_length=50)
	codpost = models.CharField(max_length=50)
=======
	num_empleado = models.CharField("Número de Empleado", max_length=50, primary_key=True)
	# puesto =models.ForeignKey(Puesto, null=False, blank=False, on_delete=models.CASCADE)
	puesto = models.CharField("Puesto", max_length=50, choices=PUESTOS)
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
>>>>>>> 9e13f78b6bada44802cce86d864b45ae8531174b

	def __str__(self):
		return f"{self.num_empleado} - {self.nombre} {self.apellido_paterno} {self.apellido_materno}"
