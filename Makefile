run:
	poetry run python player/manage.py runserver

migrate:
	poetry run python player/manage.py migrate

makemigrations:
	poetry run python player/manage.py makemigrations