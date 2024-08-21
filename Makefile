.PHONY: test
test:
	poetry run pytest

.PHONY: start
start:
	poetry run python3 mill_game/main.py
