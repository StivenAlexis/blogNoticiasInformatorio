from django.db import models

# Create your models here.

class Noticias(models.Model):
  titulo = models.CharField(max_length=200)
  subtitulo = models.CharField(max_length=255, blank=True, null=True)
  fecha_publicacion = models.DateTimeField(auto_now_add=True)
  cuerpo = models.TextField()

def __str__(self):
        return self.titulo