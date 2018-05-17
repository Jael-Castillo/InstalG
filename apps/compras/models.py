from apps.proveedores.models import Proveedor
from apps.materiales.models import Material
from django.db import models


# Create your models here.
class Compra(models.Model):
	"""docstring for Compras"""
	folio = models.CharField(max_length=50, primary_key=True)
	probeveedor = models.ForeignKey(Proveedor, null=False, blank=False, on_delete=models.CASCADE)#relación con llave primaria Proveedor
	total = models.IntegerField()
	iva_compra = models.IntegerField()

#Tabla intermedia
class Detalle_Compra(models.Model):
	"""docstring for Detalle_Compra"""
	folio_compra= models.ManyToManyField(Compra)#muchos a muchos conexión al modelo Compra
	id_material = models.ManyToManyField(Material)#muchos a muchos conexión al modelo Material
	nombre_material= models.CharField(max_length=50, primary_key=True)
	precio_unitario= models.DecimalField(max_digits=5, decimal_places=2)
	cantidad_material = models.IntegerField()
	subtotal = models.DecimalField(max_digits=5, decimal_places=2)