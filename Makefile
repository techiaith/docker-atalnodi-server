default: build

config:
	mkdir -p ${PWD}/models/


build: config
	@docker compose up --build --no-start


run:
	sudo rm -rf ${PWD}/logs
	mkdir -p ${PWD}/logs/
	@docker compose up -d --build && docker compose logs -f


stop:
	@docker compose stop


clean: stop
	@docker compose down --rmi all


purge: clean
	sudo rm -rf data
