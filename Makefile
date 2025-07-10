PYTHON=poetry run python
PYTEST=poetry run pytest

 test:
	$(PYTEST) -v

lint:
	poetry run ruff .

migrate:
	$(PYTHON) manage.py migrate

makemigrations:
	$(PYTHON) manage.py makemigrations

run:
	$(PYTHON) manage.py runserver


format:
	poetry run black .

install:
	poetry install

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -name "*.pyc" -delete