from django.db import models

# Create your models here.
class Usuario(object):
	"""docstring for Usuario"""
	num_empledo = models.CharField(max_length=50, primary_key=True)
	folio = models.CharField(max_length=15)