from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import FormularioRegistroUsuario
from . import views


#class RegistroUsuario(CreateView):
#    template_name = 'usuarios/registro.html'
#    form_class = FormularioRegistroUsuario
#    success_url = reverse_lazy('home')


def registro(request):
    if request.method== 'POST':
        form = FormularioRegistroUsuario(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            return redirect(reverse_lazy('home'))
        else:
            return render(request, 'usuarios/registro.html', {'form':form})
    else:
        form = FormularioRegistroUsuario()
        return render(request, 'usuarios/registro.html', {'form':form})



def perfiles(request, username):
    perfiles = perfiles.objects.get(user__username=username)
    return render(request, 'perfiles.html', {'perfiles': perfiles})
