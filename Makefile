# Makefile basado en https://github.com/python/python-docs-es/blob/3.8/Makefile

# start: Levantar contenedores
start:
		docker-compose start

# stop: Parar contenedores
stop:
		docker-compose stop

# logs: Mostrar logs de últimos 100 minutos por consola
logs:
		docker logs --since 100m -f enredarte_web_1

# bash: Abrir un bash dentro del contenedor
bash:
		docker-compose exec web bash

# root-bash: Abrir un bash como root dentro del contenedor
root-bash:
		docker-compose exec -u root web bash

# shell: Correr django shell_plus dentro del contenedor
shell:
		docker-compose exec web python manage.py shell_plus

# test: Correr suite de tests de django
test:
		docker-compose exec web python -m pytest

.PHONY: start stop logs bash root-bash shell test
