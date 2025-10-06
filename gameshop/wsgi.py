import os

from django.core.wsgi import get_wsgi_application

# For development use:
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gameshop.settings')

# For production use:
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gameshop.settings.production')

application = get_wsgi_application()
