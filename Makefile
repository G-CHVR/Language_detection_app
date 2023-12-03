# Makefile
DOCKER_IMAGE_NAME = language-prediction-app
PORT = 80

.PHONY: test docker_build

test:
	python3 -m unittest discover -s app -p 'test_*.py'

docker_build:
	docker build -t $(DOCKER_IMAGE_NAME) .

docker_save:
	docker save -o $(DOCKER_IMAGE_NAME).tar $(DOCKER_IMAGE_NAME)

docker_load:
	docker load -i $(DOCKER_IMAGE_NAME).tar

docker_local_run:
	docker run -p 80:80 $(DOCKER_IMAGE_NAME)