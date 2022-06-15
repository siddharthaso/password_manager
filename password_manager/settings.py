
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv('password_manager/.env')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ["*"]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'user_profile',
    'password',
    'general',

    #for Debug toolbar
    # 'debug_toolbar',
]

# INTERNAL_IPS = [
#     # ...
#     "127.0.0.1",
#     # ...
# ]

MIDDLEWARE = [
    #debug toolbar
    # The order of MIDDLEWARE is important. You should include the Debug Toolbar middleware as early as possible in the list. However, 
    # it must come after any other middleware that encodes the response’s content, such as GZipMiddleware.
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'password_manager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR /"templates"],
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

WSGI_APPLICATION = 'password_manager.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql',
        'NAME':'postgres',  
        'USER':'postgres',
        'PASSWORD':'Siddpgad[]@',
        'HOST':'db',
        'PORT':'5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_ROOT = os.path.join(BASE_DIR, 'profile_pictures')
MEDIA_URL = ''


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "user_profile:home"
LOGOUT_REDIRECT_URL = "user_profile:home"

CRISPY_TEMPLATE_PACK = 'uni_form' #bootstrap4


#EMAIL settings-----------------------------------------------------------------------------
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True    #Whether to use a Transport Layer Security (secure) connection when talking to the SMTP server. 
#This is used for explicit TLS connections, generally on port 587. If you are experiencing hanging 
# connections, see the implicit TLS setting EMAIL_USE_SSL.
EMAIL_HOST_USER = 'sunsharma492@gmail.com' #'tracy.rippin29@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('PASSWORD')

#DEBUG toolbar ---------------------------------------------------------------------------------------
# def show_toolbar(request):
#     return True

# DEBUG_TOOLBAR_CONFIG = {
#     "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
# }
# SHOW_TOOLBAR_CALLBACK = show_toolbar

# DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False,}


# DJANGO_DEBUG = True 

# DEBUG_TOOLBAR_CONFIG = {'INSERT_BEFORE':'</head>'}

# DEBUG_TOOLBAR_PANELS = [
#     'debug_toolbar.panels.history.HistoryPanel',
#     'debug_toolbar.panels.versions.VersionsPanel',
#     'debug_toolbar.panels.timer.TimerPanel',
#     'debug_toolbar.panels.settings.SettingsPanel',
#     'debug_toolbar.panels.headers.HeadersPanel',
#     'debug_toolbar.panels.request.RequestPanel',
#     'debug_toolbar.panels.sql.SQLPanel',
#     'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#     'debug_toolbar.panels.templates.TemplatesPanel',
#     'debug_toolbar.panels.cache.CachePanel',
#     'debug_toolbar.panels.signals.SignalsPanel',
#     'debug_toolbar.panels.logging.LoggingPanel',
#     'debug_toolbar.panels.redirects.RedirectsPanel',
#     'debug_toolbar.panels.profiling.ProfilingPanel',
# ]

#Celery settings------------------------------------------------------------------
# CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
# CELERY_ACCEPT_CONTENT = ['application/json']
# # accept_content = ['application/json']

# CELERY_BROKER_URL = 're://127.0.0.1:6379'

# CELERY_RESULT_SERIALIZER = 'json'
# # result_serializer = 'json'

# CELERY_TASK_SERIALIZER = 'json'
# # task_serializer = 'json'

# CELERY_TIMEZONE = "Asia/Kolkata"
# # timezone = "Asia/Kolkata"


# CELERY_TASK_TRACK_STARTED = True
# CELERY_TASK_TIME_LIMIT = 30 * 60

# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
# result_backend = 'redis://127.0.0.1:6379'

#CELERY BEAT
# CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

#TO avoide warnings
# celery upgrade settings path/to/settings.py