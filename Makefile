#!make
# Default values, can be overridden either on the command line of make
# or in .env

# .PHONY: init vars test coverage \
# 	version vars ps \
# 	build pull changelog \
# 	release push-qa push-prod

.PHONY:

lint:
	flake8 backend/

test: lint
	pytest

run:
	uvicorn backend.main:app --reload

