from django.db import models

# Create your models here.
class Alumno(models.Model):
	nombre = models.CharField( max_length=50, help_text='Ingrese nombre')
	apellido = models.CharField( max_length=50, help_text='Ingrese apellido')

class Curso(models.Model):
	titulo = models.CharField( max_length=50)
