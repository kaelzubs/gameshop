#!/bin/bash

set -e
python manage.py migrate
python manage.py makesuperuser

sudo chown -R www-data:www-data /code/mediafiles
sudo chmod -R 775 /code/mediafiles