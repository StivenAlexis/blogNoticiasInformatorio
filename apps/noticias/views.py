from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Noticias

class CrearNoticia(CreateView):
    model = Noticias
    fields = ['titulo', 'cuerpo']
    template_name = 'noticias/crear_noticia.html'

class ListarNoticias(ListView):
    model = Noticias
    template_name = 'noticias/lista_noticias.html'
    context_object_name = 'noticias'


class DetalleNoticia(DetailView):
    model = Noticias
    template_name = 'noticias/detalle.html'

class EditarNoticia(UpdateView):
    model = Noticias
    fields = ['titulo', 'cuerpo']  
    template_name = 'noticias/editar_noticia.html'

class EliminarNoticia(DeleteView):
    model = Noticias
    success_url = reverse_lazy('listar_noticias')  # Reemplaza con la URL de tu lista de noticias
    template_name = 'noticias/eliminar_noticia.html'