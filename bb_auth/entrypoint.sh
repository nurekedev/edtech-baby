python manage.py migrate
python manage.py collectstatic --no-input
exec gunicorn bb_auth.wsgi:application --bind 0.0.0.0:8000 --timeout 120 --workers=3 --log-level info
