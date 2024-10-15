from .base import * 


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--x-d26q-a=k0_c3!kb-te5nv!s-7g-f38p03u)i=@-f%gmu20-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}