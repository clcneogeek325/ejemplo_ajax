from django.db import models


class verduras(models.Model):
	nombre = models.CharField(max_length=100)
	status = models.BooleanField(default=True)
	def __unicode__(self):
		return self.nombre


class frutas(models.Model):
	nombre = models.CharField(max_length=100)
	status = models.BooleanField(default=True)
	def __unicode__(self):
		return self.nombre


