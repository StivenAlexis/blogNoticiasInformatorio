from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioRegistroUsuario(UserCreationForm):
    #first_name = forms.CharField(label='Nombre', required=True)
    #last_name = forms.CharField(label='Apellido', required=True)
    #username = forms.CharField(label='Usuario', required=True)
    #email = forms.EmailField(label='Correo', required=True)
    #password1 = forms.CharField(
       #label='Contraseña', widget=forms.PasswordInput, required=True)
    #password2 = forms.CharField(
        #label='Confirmar Contraseña', widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]