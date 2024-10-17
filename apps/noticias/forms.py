from django import forms
from .models import Noticias

class FormularioCrearNoticia(forms.ModelForm):

    class Meta:
        model = Noticias
        fields = ('titulo','fecha_publicacion','imagen',"categoria", "cuerpo")


class FormularioModificarNoticia(forms.ModelForm):

    class Meta:
        model = Noticias
        fields = ('autor','imagen','categoria', "cuerpo")