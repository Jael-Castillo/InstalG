from django.db import models


class UsuarioDepartamento(models.Model):
    rfc = models.CharField("RFC", max_length=13, primary_key=True)
    nombre = models.CharField("Nombre", max_length=50)
    apellido_paterno = models.CharField("Apellido Paterno", max_length=50)
    apellido_materno = models.CharField("Apellido Materno", max_length=50)

    class Meta:
        ordering = ['apellido_paterno', 'apellido_materno']

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"
