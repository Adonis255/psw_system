#!/usr/bin/env bash
# exit on error
set -o errexit

# Disable automatic collectstatic
export DISABLE_COLLECTSTATIC=1

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Create a superuser if it doesn't exist
echo "from django.contrib.auth.models import User; User.objects.create_superuser('MERCY', 'mercy254255@gmail.com', 'sucre123') if not User.objects.filter(username='MERCY').exists() else None" | python manage.py shell