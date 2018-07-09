from django.db import models


class Prestador(models.Model):
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    celular = models.CharField(max_length=10)
    email = models.EmailField()
    pais = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    foto_perfil = models.ImageField(upload_to='perfiles')
    descripcion = models.TextField()
    pagina_web = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='Actualizado')

    class Meta:
        verbose_name = 'Prestador'
        verbose_name_plural = 'Prestadores'

    def __str__(self):
        return self.nombres + ' ' + self.apellidos
