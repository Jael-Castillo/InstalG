from apps.proveedores.models import Proveedor, Material;
from django.db import models


# Create your models here.
class Compra(models.Model):
	"""docstring for Compras"""
	folio_compra = models.CharField(max_length=50, primary_key=True)
	id_fk_probeveedor = models.ForeignKey(Proveedor, null=False, blank=False, on_delete=models.CASCADE)#relación con llave primaria Proveedor
	total = models.IntegerField()
	iva_compra = models.IntegerField()

#Tabla intermedia
class Detalle_Compra(models.Model):
	"""docstring for Detalle_Compra"""
	folio_compra_pk_fk = models.ManyToManyField(Compra)#muchos a muchos conexión al modelo Compra
	id_material_pk_fk = models.ManyToManyField(Material)#muchos a muchos conexión al modelo Material
	nombre_material= models.CharField(max_length=50, primary_key=True)
	precio_unitario= models.DecimalField(max_digits=5)
	cantidad_material = models.IntegerField()
	sub_total = models.DecimalField(max_digits=5)