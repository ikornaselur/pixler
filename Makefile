mypy:
	poetry run mypy pixler tests

flake8:
	poetry run flake8 pixler tests

lint: mypy flake8

test:
	poetry run pytest tests -sv
