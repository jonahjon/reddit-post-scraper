#!make
# Default values, can be overridden either on the command line of make
# or in .env

.PHONY: init vars test coverage \
	version vars ps \
	build pull changelog \
	release push-qa push-prod

test:
	cd test && pytest

run:
 	uvicorn main app --reload