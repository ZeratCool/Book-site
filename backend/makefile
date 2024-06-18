migrate:
	python manage.py makemigrations && python manage.py migrate

run:
	python manage.py runserver

g_run:
	gunicorn backend.wsgi:application -b 0.0.0.0:8000