
from django.urls import path
from django.contrib.auth import views as auth
from . import views

app_name = 'usuarios'

urlpatterns = [
    
    path('registro/',views.registro, name = 'registro'),
    path('perfiles/<str:username>/', views.perfiles, name='perfiles.html'),
    path('Login/', auth.LoginView.as_view(template_name='usuarios/login.html'),name = 'login'),
    path('Logout/', auth.LogoutView.as_view(),name = 'logout'),

]


