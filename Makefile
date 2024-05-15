build:
	docker-compose -f docker-compose.yml up -d --build
down:
	docker-compose -f docker-compose.yml down


lint:
	poetry run black .
	poetry run ruff check .
	poetry run mypy .
	poetry run isort .

check-migrations:
	oetry run dj makemigrations --check

test:
	try run pytest

ci: lint check-migrations test
