.PHONY: test
test:
	coverage run --omit="tests/*" -m pytest
	pre-commit run --files dotty/*
	mypy dotty
	coverage report -m

.PHONY: install-hooks
install-hooks:
	pre-commit install --install-hooks --overwrite

.PHONY: clean
clean:
	rm -drf .pytest_cache/ .mypy_cache/ .coverage
