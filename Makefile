mypy:
	poetry run mypy pixler

flake8:
	poetry run flake8 pixler

lint: mypy flake8

test:
	poetry run pytest tests -sv
