#!/bin/bash

set -e
gunicorn gameshop.wsgi --log-file -