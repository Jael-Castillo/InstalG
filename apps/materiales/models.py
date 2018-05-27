from django.db import models

# Create your models here.

class Material(models.Model):
	"""docstring for Material"""
	material = models.CharField(max_length=50, primary_key=True)
	nombre= models.CharField(max_length=50)
	existencia= models.IntegerField()
	descripcion= models.CharField(max_length=50)


