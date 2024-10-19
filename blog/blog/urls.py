from django.contrib import admin 
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.Home, name = 'home'),
    path('admin/', admin.site.urls),
    path('admin_redirect/', views.AdminRedirect, name="admin_redirect"),
    
    
    path('login/', 
         auth_views.LoginView.as_view(template_name="usuarios/login.html"),
         name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name = 'logout'),
    path('sobrenosotros/', views.SobreNosotros, name = 'sobrenosotros'),
    path('preguntasFQ/', views.PreguntasFQ, name = 'preguntasFQ'),
    path('noticia_detalles/', views.NoticiaDetalles, name = 'noticia_detalles'),

    
    path('Noticias/', include('apps.noticias.urls')),
    path('Usuarios/', include('apps.usuarios.urls')),
    path('Contacto/', include('apps.contacto.urls')),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
