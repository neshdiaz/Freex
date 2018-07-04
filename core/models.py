from django.db import models


class Prestador(models.Model):
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    celular = models.CharField(max_length=10)
    email = models.EmailField()
    pais = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    foto_perfil = models.ImageField()
