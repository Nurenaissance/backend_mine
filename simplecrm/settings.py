"""
Django settings for simplecrm project.

Generated by 'django-admin startproject' using Django 2.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '77fy+^i(n=2)tq$0)&31d@uf3t+ge##$aclyla&lmr@lpinc1&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*','http://127.0.0.1:9000/']


# Application definition

INSTALLED_APPS = [
    #'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'calls',
    'leads',
    'meetings',
    'opportunities',
    'contacts',
    'interaction',
    'rest_framework',
    'corsheaders',
    'tasks',
    'channels',
    'reminder',
    'simplecrm',
    'tenant',
    'campaign',
    'node_temps',
    'vendors',
    'product',
    'documents',
    'dynamic_entities',
    'loyalty',
    'custom_fields',
    'tickets',
    'stage',
    'reports',
    'api',
    'whatsapp_chat',
    'drafts',

]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'simplecrm.middleware.TenantMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
   
]

# LOGGING = {
#      'version': 1,
#      'disable_existing_loggers': False,
#      'handlers': {
#          'console': {
#              'level': 'DEBUG',  # Set the desired log level
#              'class': 'logging.StreamHandler',
#          },
#      },
#      'loggers': {
#          'django': {
#              'handlers': ['console'],
#              'level': 'DEBUG',
#              'propagate': True,
#          },
#          'simplecrm': {  # Replace 'yourapp' with the actual app name
#              'handlers': ['console'],
#              'level': 'DEBUG',
#              'propagate': True,
#          },
#      },
#  }

AUTH_USER_MODEL = 'simplecrm.CustomUser'

ROOT_URLCONF = 'simplecrm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'simplecrm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nurenpostgres', 
        'USER': 'nurenai',
        'PASSWORD': 'Biz1nurenWar*',
        'HOST': 'nurenaistore.postgres.database.azure.com', 
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require',  # Enforce SSL
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

CSRF_TRUSTED_ORIGINS = ['https://b3fa-14-142-75-54.ngrok-free.app','http://localhost:3000',"https://dea2-14-142-75-54.ngrok-free.app","http://127.0.0.1:8000" ]
# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
    'http://localhost:5173/',
)

CORS_ALLOW_ALL_ORIGINS=True
CORS_ALLOW_HEADERS = [
    'X-Tenant-Id',  # Add the headers you need to allow
    'Content-Type',
]
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173",
        # Add your React frontend URL here
    # Add other allowed origins if needed
]

ASGI_APPLICATION = 'simplecrm.asgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}
