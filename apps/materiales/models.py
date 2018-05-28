from django.db import models

from apps.proveedores.models import Proveedor


class Material(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    nombre = models.CharField("Nombre", max_length=50)
    existencia = models.CharField("Existencia", max_length=50)
    descripcion = models.CharField("Descripción", max_length=50)
    precio = models.FloatField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.nombre}"
