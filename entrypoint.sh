#! bin/sh
#Apply database migrations

python3 dashboard/manage.py makemigrations
python3 dashboard/manage.py migrate

export DJANGO_SUPERUSER_EMAIL=admin@dashboard.com

export DJANGO_SUPERUSER_PASSWORD=admin@123

export DJANGO_SUPERUSER_USERNAME=dashboardmanager

python3 dashboard/manage.py createsuperuser --no-input
python3 dashboard/manage.py collectstatic --no-input
python3 dashboard/manage.py makemigrations
python3 dashboard/manage.py migrate

# Start the Django development server
python3 dashboard/manage.py runserver 0.0.0.0:8080