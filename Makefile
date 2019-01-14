run-dev: .env
	export $(cat .env)
	source ./venv/bin/activate; \
	pip install -r requirements.txt; \
	python main.py


run-test: .env.test
	export $(cat .env.test)
	source ./venv/bin/activate; \
	pytest tests