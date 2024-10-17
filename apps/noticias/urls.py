from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path('noticia/', views.ListarNoticias.as_view(), name='listar_noticia'),
    path('noticia/<int:pk>/', views.DetalleNoticia.as_view(), name='detalle_noticia'),
    path('crear_noticia/', views.CrearNoticia.as_view(), name='crear_noticia'),
    path('editar_noticia/<int:pk>/', views.EditarNoticia.as_view(), name='editar_noticia'),
    path('eliminar_noticia/<int:pk>/', views.EliminarNoticia.as_view(), name='eliminar_noticia'), 
    
]
