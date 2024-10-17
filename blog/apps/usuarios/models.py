# Aca vamos a poner los modelos que van a impactar en la BBDD


from django.db import models

from django.contrib.auth.models import AbstractUser, Group, Permission

#class Usuario(AbstractUser):
    # aca vamos a especificar las caracteristicas especificas del modelo de
    # user.
    #pass

class User(models.Model):
    # ... other fields
    groups = models.ManyToManyField(Group, related_name='auth_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='auth_user_set')

class Usuario(models.Model):
    # ... other fields
    groups = models.ManyToManyField(Group, related_name='usuario_set')
    user_permissions = models.ManyToManyField(Permission, related_name='usuario_set')