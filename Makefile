.PHONY: debug
debug:
	python debug.py

.PHONY: tests
tests:
	pytest --cov=project/ tests/
