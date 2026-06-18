#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('MERCY', 'mercy254255@gmail.com', 'sucre123') if not User.objects.filter(username='MERCY').exists() else None" | python manage.py shell