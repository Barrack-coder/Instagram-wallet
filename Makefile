serve:
	python manage.py runserver
migrate:
	python manage.py migrate
migrations:
	python manage.py makemigrations ${name}
superuser:
	python manage.py createsuperuser --username ${name}
collectstatic:
	python manage.py collectstatic