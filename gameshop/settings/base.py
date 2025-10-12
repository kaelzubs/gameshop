import os
from decouple import config
import secrets
import string


choices = string.ascii_letters + string.digits + "<>()[]*?@!#~,.;"
key = "".join(secrets.choice(choices) for n in range(100))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = key

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

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
MEDIAFILES_DIRS = [os.path.join(BASE_DIR, 'media_in_env')]

# Auth
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)

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
ROBOTS_USE_SITEMAP = True
ROBOTS_SITEMAP_URLS = ['https://www.gameshop.com/sitemap.xml']
ROBOTS_DISALLOW_ALL = False
ROBOTS_ALLOW_ALL = True
ROBOTS_SITEMAP_URL = 'https://www.gameshop.com/sitemap.xml'
ROBOTS_HOST = 'https://www.gameshop.com'
COOKIELAW_NAME = 'CookieLawInfoConsent'
COOKIELAW_VERBOSE_NAME = 'Cookie Consent'
COOKIELAW_MAX_AGE = 31536000  # one year
COOKIELAW_PATH = '/'
COOKIELAW_SECURE = False
COOKIELAW_SAMESITE = 'Lax'
COOKIELAW_MESSAGE = 'This website uses cookies to ensure you get the best experience on our website.'
COOKIELAW_DISMISS = 'Got it!'
COOKIELAW_LEARN_MORE = 'More info'
COOKIELAW_LINK = '/privacy-policy/'
COOKIELAW_THEME = 'dark-bottom'
COOKIELAW_POSITION = 'bottom'
COOKIELAW_TYPE = 'info'
