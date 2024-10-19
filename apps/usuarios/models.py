from django.db import models
from django.contrib.auth.models import User

class perfiles(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia = models.TextField(max_length=500, blank=True)
    imagen_perfil = models.ImageField(upload_to='perfiles_pics/', default='default.jpg')

    def __str__(self):
        return f'{self.user.username} perfiles'
