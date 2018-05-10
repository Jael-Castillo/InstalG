from django.db import models

# Create your models here.

class Proveedores(models.Model):
	id_probeveedor = models.CharField(max_length=50, primary_key=True)
	nombre_prov = models.CharField(max_length=50)
	apellido_prov = models.CharField(max_length=50)
	nombre_empresa = models.CharField(max_length=30)
	estatus_pedido = models.CharField(max_length=10)