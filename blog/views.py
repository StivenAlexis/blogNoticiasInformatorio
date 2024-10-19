from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LogoutView


def Home(request):

    return render(request,'base.html')

def AdminRedirect(request):
    return HttpResponseRedirect('/admin')

def Login(request):
    return render(request, 'usuarios/login.html')

def Register(request):
    return render(request, 'usuarios/registro.html')


def NoticiaDetalles(request):
    return render(request, 'noticias/ModalNoticias.html')

def SobreNosotros(request):
    return render(request, 'sobre nosotros/about_us.html')

def PreguntasFQ(request):
    return render(request, 'sobre nosotros/faq.html')

class LogoutView(LogoutView):
    template_name = 'accounts/logout.html'