DC = docker compose
STORAGES_FILE = docker-compose/storage.yaml
EXEC = docker exec -it
DB_CONTAINER = example-db
LOGS = docker logs
ENV = --env-file .env
APP_FILE = docker-compose/app.yaml
APP_CONTAINER = main-app


.PHONY: app
app:
	${DC} -f ${APP_FILE} ${ENV} up --build -d


.PHONY: app-shell
app-shell:
	${EXEC} ${APP_CONTAINER} bash


# .PHONY: app-logs
# app-logs:
# 	${LOGS} ${APP_CONTAINER} -f


.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} -f ${STORAGES_FILE} down