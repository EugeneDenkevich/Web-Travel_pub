SHELL=/bin/bash

run:
	cp backend/.env-example backend/.env

up:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py collectstatic --noinput
	python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); print('User already exists') if User.objects.filter(email='user@user.ru').exists() else User.objects.create_superuser('user@user.ru', '123123') and print('User was created')" 
	python manage.py runserver 0.0.0.0:8000