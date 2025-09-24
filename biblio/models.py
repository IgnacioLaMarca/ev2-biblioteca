from django.db import models

# Modelo que representa un libro en la biblioteca
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    num_paginas = models.IntegerField()
    copias_disponibles = models.IntegerField(default=1)

    def __str__(self):
        return self.titulo

# Modelo que representa un miembro de la biblioteca
class Miembro(models.Model):
    nombre = models.CharField(max_length=100)
    numero_identificacion = models.CharField(max_length=50, unique=True)
    libros_prestados = models.ManyToManyField(Libro, blank=True)

    def __str__(self):
        return self.nombre

# Modelo que representa la biblioteca en sí misma
class Biblioteca(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    # Métodos básicos
    def buscar_libro(self, titulo):
        return Libro.objects.filter(titulo__icontains=titulo)

    def prestar_libro(self, libro, miembro):
        if libro.copias_disponibles > 0:
            libro.copias_disponibles -= 1
            libro.save()
            miembro.libros_prestados.add(libro)
            return True
        return False

    def devolver_libro(self, libro, miembro):
        if libro in miembro.libros_prestados.all():
            libro.copias_disponibles += 1
            libro.save()
            miembro.libros_prestados.remove(libro)
            return True
        return False

    def __str__(self):
        return self.nombre
