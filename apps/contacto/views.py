from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

def contactanos(request):
    return render(request, 'contactos/contact_form.html')

def enviar_contacto(request):
    nombre = request.POST['contacto_nombre_name']
    mensaje = request.POST['contacto_mensaje_name']
    email = request.POST['contacto_email_name']
    telefono = request.POST['contacto_telefono_name']
    
    form_data = {
        'nombre':nombre,
        'email':email,
        'telefono':telefono,
        'mensaje':mensaje,
        }
    mensaje = f'''
    Desde:\n\t\t{form_data['nombre']}\n
    Mensaje:\n\t\t{form_data['mensaje']}\n
    Email:\n\t\t{form_data['email']}\n
    Telefono:\n\t\t{form_data['telefono']}\n
    '''
    if settings.DEBUG:
        return render(request, 'base.html')
    else:
        send_mail('Solicitud de contacto desde Noticias Chacú', mensaje, '',
              ['MAILTEMPORAL@GMAIL.com'])
        return render(request, 'base.html')