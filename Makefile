update-pip:
	@pip install --upgrade pip

install: update-pip requirements.txt
	@pip install -r requirements.txt

install-dev: requirements-dev.txt
	@pip install -r requirements-dev.txt

run:
	@python manage.py run

test:
	@python -m pytest
