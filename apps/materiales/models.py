from django.db import models

# Create your models here.

class Material(models.Model):
	"""docstring for Material"""
	id_material = models.CharField(max_length=50, primary_key=True)
	nombre_material = models.CharField(max_length=50)
	existencia_material = models.IntegerField()
	descripción_material = models.CharField(max_length=50)


