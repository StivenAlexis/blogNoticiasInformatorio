from django.contrib import admin

from .models import Comentario, Noticia, Categoria

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "imagen", "cuerpo")
    


# en el sitio 'admin' registrar 'Noticia' y 'Categoria'
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Categoria)
admin.site.register(Comentario)

