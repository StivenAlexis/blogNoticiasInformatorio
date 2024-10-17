from django.contrib import admin

from .models import Comentario, Noticia, Categoria


# en el sitio 'admin' registrar 'Noticia' y 'Categoria'
admin.site.register(Noticia)
admin.site.register(Categoria)
admin.site.register(Comentario)

