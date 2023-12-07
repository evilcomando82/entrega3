from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre
    
class Curso(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120)
    pais_origen =models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)
    curso_origen =models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

