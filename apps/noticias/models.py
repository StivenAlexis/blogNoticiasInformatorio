from django.db import models


# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=250)
    def __str__(self):
        return self.nombre

class Noticias(models.Model):
  titulo = models.CharField(max_length=200)
  subtitulo = models.CharField(max_length=255, blank=True, null=True)
  fecha_publicacion = models.DateTimeField(auto_now_add=True)
  cuerpo = models.TextField()
  imagen = models.ImageField(upload_to='noticias', null = True)
  categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null= True)

def __str__(self):
        return self.titulo