from .base import *

#OCULTAR ESTA CLAVE
SECRET_KEY = 'django-insecure-%ujzgm923y)sew7b&08$e(+m%jx6*jb$11-5wd@f=q+p=*lk+('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#DOMINIO PERMITIDO, EJE: www.informatorio.com.ar
ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


#CONFIGURACION REAL DE LA BD DE PRODUCCION
#CONFIGURAR USUARIOS Y CONTRASEÑAS Y PUERTOS.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',  # or your database server address
        'PORT': '3306',
    }
}


STATICFILES_DIRS = (BASE_DIR, 'static')