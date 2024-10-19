from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import perfiles

@receiver(post_save, sender=User)
def create_user_perfiles(sender, instance, created, **kwargs):
    if created:
        perfiles.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_perfiles(sender, instance, **kwargs):
    instance.perfiles.save()

