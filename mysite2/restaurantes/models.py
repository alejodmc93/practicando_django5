from django.db import models

class Restaurate(models.Model):
	nombre = models.CharField(max_length=100)
	ubicacion = models.CharField(max_length=100)
	telefono = models.CharField(max_length=8)

	STATUS_ACTIVE = 1
	STATUS_DELETED = 2

	STATUS_CHOICES = (
			(STATUS_ACTIVE,'activo'),
			(STATUS_DELETED,'eliminado'),
		)
	status = models.SmallIntegerField(
			choices = STATUS_CHOICES,
			default = STATUS_ACTIVE,
		)
	def __str__(self):
		return self.nombre

class Menu(models.Model):
	restaurate = models.ForeignKey(Restaurate)
	plato = models.CharField(max_length=100)
	def __str__(self):
		return self.plato

