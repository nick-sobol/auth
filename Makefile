#
# Makefile for authentication test project
#

.PHONY: help
help:
	@echo 'Makefile for BU Sanic playground'
	@echo ''
	@echo '1. Building:'
	@echo '  make setup         Build your environment and setup project'
	@echo ''
	@echo '2. Testing:'
	@echo '  make run-test          Run tests'
	@echo ''
	@echo '3. Running:'
	@echo '  make run-dev       Run locally using dev server'
	@echo ''


.PHONY: setup
setup: clean
	python3 -m venv venv; \
	source venv/bin/activate; \
	pip install -r requirements.txt

.PHONY: clear
clean:
	@rm -rf venv/

.PHONY: run-dev
run-dev: .env_test
	export $(shell cat .env_test); \
	source ./venv/bin/activate; \
	python main.py

.PHONY: run-test
run-test: .env_test
	export $(shell cat .env_test); \
	source ./venv/bin/activate; \
	pytest tests
