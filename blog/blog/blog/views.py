from django.shortcuts import render
from django.http import HttpResponseRedirect


def Home(request):

    return render(request,'base.html')

def SobreNosotros(request):
    return render(request, 'sobre nosotros/sobre_nosotros.html')

def AdminRedirect(request):
    return HttpResponseRedirect('/admin')

def PreguntasFQ(request):
    return render(request, 'sobre nosotros/preguntas_frecuentes.html')

def NoticiaDetalles(request):
    return render(request, 'noticias/ModalNoticias.html')