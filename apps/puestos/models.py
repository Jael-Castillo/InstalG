from django.db import models


# Create your models here.
class Puesto(models.Model):
	"""docstring for Puesto"""
	puesto =models.CharField(max_length=50, primary_key=True)
	nombre= models.CharField(max_length=20)
	estado = models.BooleanField(default=True)