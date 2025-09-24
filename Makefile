install:
	poetry install

lint:
	poetry run black src tests
	poetry run flake8 src tests
	poetry run mypy src

test:
	poetry run pytest -v

run-api:
	poetry run uvicorn src.serving.app:app --reload

