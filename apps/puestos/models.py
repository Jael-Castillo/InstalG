from django.db import models


class Puesto(models.Model):
    nombre = models.CharField(max_length=20)
    estado = models.BooleanField("Activo", default=True)
    tipo_contrato = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre}"