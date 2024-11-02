#!/bin/bash
set -e

# Run migrations
python manage.py migrate --noinput

# Collect static files (for production)
if [ "$ENVIRONMENT" = "production" ]; then
  python manage.py collectstatic --no-input
fi

# Create admin user
python manage.py createsuperuser --no-input || echo "Superuser creation failed."

# Start the application
if [ "$ENVIRONMENT" = "production" ]; then
  exec gunicorn core.wsgi:application \
    --bind 0.0.0.0:8000 -w 2 --log-level info \
    --access-logfile ./logs/gunicorn.access.log \
    --error-logfile ./logs/gunicorn.error.log
else
  exec python manage.py runserver 0.0.0.0:8000
fi
