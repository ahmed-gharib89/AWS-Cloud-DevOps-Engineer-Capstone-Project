install:
	pip install --upgrade pip && \
		pip install -r requirements.txt

format:
	black urlshort/*.py

lint:
	docker run --rm -i hadolint/hadolint < Dockerfile
	pylint --disable=R,C,W1203,W0702 urlshort/app.py

test:
	coverage run -m pytest 

build:
	docker-compose build --no-cache

run:
	docker-compose up -d

invoke:
	curl http://10.0.0.11:30000


all: install lint test