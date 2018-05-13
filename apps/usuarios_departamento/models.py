from django.db import models

# Create your models here.
class Usuario_Departamento(models.Model):
	"""docstring for Usurio_Departamento"""
	rfc = models.CharField(max_length=50, primary_key=True)
	nombre_usuario = models.CharField(max_length=50)
	apellido_pat = models.CharField(max_length=50)
	apellido_mat = models.CharField(max_length=50)