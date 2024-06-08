import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y8f=0-@pcbn456fdgdfvm8a2*!9rd#07fryk*a-nwvy5xxga(v^%3t0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #installed
    'widget_tweaks',
    
    'profiles',
    'events',
    'base'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'source.urls'

TEMPLATES = [
    {
        'BACKEND' : 'django.template.backends.django.DjangoTemplates',
        'DIRS'    : [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS' : {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'source.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE     = 'UTC'
USE_I18N      = True
USE_L10N      = True
USE_TZ        = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / 'staticFiles']
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "staticDir", "mediaFiles")


# STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]


STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]


# Media settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# login settings for login aster failed login
LOGIN_URL = 'accounts/login/'
LOGOUT_URL = '/logout/'

# login settings for redirecting ater successfull login

LOGIN_REDIRECT_URL  = 'home:home'
LOGOUT_REDIRECT_URL = 'home:home'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# configuration For Sending Email with SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'astroevents0@gmail.com'   
EMAIL_HOST_PASSWORD = 'tton rxoy klzx jxho'  # app password for 'astroevents0@gmail.com'
DEFAULT_FROM_EMAIL = 'astroevents0@gmail.com'

# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST_USER = "bryansine1738@gmail.com"  # Login email
# EMAIL_HOST_PASSWORD = 'gqemhqaxznoyykgs'  # App-specific password
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587

# DEFAULT_FROM_EMAIL = 'astroevents0@gmail.com'  # Email that users will see


# #configuration For Sending Email with SMTP
# EMAIL_HOST          = 'smtp.gmail.com'
# EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST_USER     = "bryansine1738@gmail.com" # Email
# EMAIL_HOST_PASSWORD = 'gqemhqaxznoyykgs' # Password
# EMAIL_USE_TLS       = True
# EMAIL_PORT          = 587


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'apikey'
# EMAIL_HOST_PASSWORD = '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'
# DEFAULT_FROM_EMAIL = 'bryansine1738@gmail.com'
# SERVER_EMAIL = 'bryansine1738@gmail.com'




