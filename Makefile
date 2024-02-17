build:
	docker compose build
restart:
	docker compose up --force-recreate -d

stop:
	docker compose stop