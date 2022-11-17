.PHONY:
init: down volume up install_dependencies
down:
	docker-compose down
volume:
	docker volume prune -f
pull:
	docker-compose pull
build:
	docker-compose build
up: pull build
	docker-compose up -d
	make ps
ps:
	docker-compose ps
test:
	python -m pytest
prune:
	make down
	docker volume prune -f
	docker system prune -f
	rm -rf .dynamodb/*
lint:
	docker-compose run --rm core sh -c "python -m pycln src -a -s && black src/ && isort src/ --profile black && flake8 src/"
install_dependencies:
	pip install -r requirements.txt
