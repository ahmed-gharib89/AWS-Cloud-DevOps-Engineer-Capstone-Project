install:
	pip install --upgrade pip && \
		pip install -r requirements.txt

lint:
	docker run --rm -i hadolint/hadolint < Dockerfile
	pylint --disable=R,C,W1203,W0702 urlshort/urlshort.py

test:
	python -m pytest -vv --cov=app urlshort/test_main.py

build:
	docker-compose build --no-cache

run:
	docker-compose up -d

invoke:
	curl http://localhost:5000


all: install lint test