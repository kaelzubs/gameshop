#!/bin/bash
# Startup script for production server
# Collect static files and start Gunicorn server
python manage.py collectstatic && gunicorn --workers 2 gameshopa.wsgi