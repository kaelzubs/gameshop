import os
from decouple import config
import secrets
import string
import dj_database_url

# Generate a secure random secret key
choices = string.ascii_letters + string.digits + "<>()[]*?@!#~,.;"
key = "".join(secrets.choice(choices) for n in range(100))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECRET_KEY = key
SECRET_KEY = config('SECRET_KEY', default=key)

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = []
if DEBUG == True:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']
elif DEBUG == False:
    ALLOWED_HOSTS = ['.applikuapp.com']
ALLOWED_HOSTS = ['gameshop.applikuapp.com', 'www.gameshop.applikuapp.com']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',

    'core',
    'robots',
    'cookielaw',
    'django.contrib.sitemaps',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
    'django.middleware.gzip.GZipMiddleware',
]

ROOT_URLCONF = 'gameshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'gameshop.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIAFILES_DIRS = [os.path.join(BASE_DIR, 'media')]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')


WHITENOISE_KEEP_ONLY_HASHED_FILES = True
WHITENOISE_MAX_AGE = 31536000  # One year in seconds
WHITENOISE_IMMUTABLE_FILE_TEST = lambda path, url: url.startswith(STATIC_URL)
WHITENOISE_ALLOW_ALL_ORIGINS = True
WHITENOISE_USE_FINDERS = True
WHITENOISE_AUTOREFRESH = DEBUG
WHITENOISE_ROOT = STATIC_ROOT
WHITENOISE_MIMETYPES = {
    '.js': 'application/javascript',
    '.css': 'text/css',
}
    
STATICFILES_STORAGE = "gameshop.storage.WhiteNoiseStaticFilesStorage"
MEDIAFILES_STORAGE = "gameshop.storage.MediaStorage"

STORAGES = {
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}

# DATABASE_URL = config('DATABASE_URL')
DATABASE_URL = config('DATABASE_URL')
if DEBUG == True:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
elif DEBUG == False:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
        }
    }
DATABASES['default'] = dj_database_url.parse(DATABASE_URL, conn_max_age=600)

# Auth
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

SITE_ID = 1

# CRISPY FORMS
CRISPY_TEMPLATE_PACK = 'bootstrap4'

DEFAULT_AUTO_FIELD='django.db.models.AutoField'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'Email recieved from gameshop.com'
DEFAULT_FROM_EMAIL = 'kaelzubs@gmail.com'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

MAILCHIMP_API_KEY = config('MAILCHIMP_API_KEY')
MAILCHIMP_DATA_CENTER = config('MAILCHIMP_DATA_CENTER')
MAILCHIMP_EMAIL_LIST_ID = config('MAILCHIMP_EMAIL_LIST_ID')

ROBOTS_CACHE_TIMEOUT = 60*60*24
