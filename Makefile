.PHONY: test
test:
	poetry run pytest

.PHONY: start
start:
	poetry run python3 mill_game/main.py

.PHONY: lint
lint:
	poetry run ruff check mill_game tests
	poetry run ruff format mill_game tests --check
	poetry run mypy -p mill_game
	poetry run mypy -p tests

.PHONY: format
format:
	poetry run ruff format mill_game tests
