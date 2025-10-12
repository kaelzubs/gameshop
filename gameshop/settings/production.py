from .base import *
from decouple import config
import dj_database_url

DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = ['gameshop.onrender.com', 'gameshop-9nk6.onrender.com']



AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': config('DB_PORT')
#     }
# }

DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://gameshop_rcll_user:jIHt3ZWcPkGGpbJCDrr8hFQcMiDYTULD@dpg-d3hn07e3jp1c73fm41j0-a.oregon-postgres.render.com/gameshop_rcll',
        conn_max_age=600,
        ssl_require=True
    )
}