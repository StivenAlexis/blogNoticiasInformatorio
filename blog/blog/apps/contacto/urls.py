from django.urls import path

from . import views

app_name = 'contactos'
# la url comienza con /contactos.. (ver apps\noticias\views.py)
urlpatterns = [
    path('contactanos/', views.contactanos, name = 'contactanos'),
    path('contactanos/enviar_contacto', views.enviar_contacto, 
         name = 'enviar_contacto')
]