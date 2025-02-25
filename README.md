# Используемый стек технологий.
- ![Python](https://img.shields.io/badge/-Python-black?style=flat-square&logo=Python)
- ![Django](https://img.shields.io/badge/-Django-0aad48?style=flat-square&logo=Django)
- ![Django Rest Framework](https://img.shields.io/badge/DRF-red?style=flat-square&logo=Django)
- ![Static Badge](https://img.shields.io/badge/Swagger-lightgreen)
- ![Docker](https://img.shields.io/badge/-Docker-46a2f1?style=flat-square&logo=docker&logoColor=white)
- ![Static Badge](https://img.shields.io/badge/Docker-compose-blue)

# Описание.
Сайт для создания базы музыкантов/исполнителей и их альбомов и песен.

# Инструкция для запуска.

## Переменная окружения.
В корневой папке создать файл расширения _.env.docker_
```
SECRET_KEY=XXXXXX
DEBUG=XXXX
ALLOWED_HOSTS=XXXXXX XXXXXXX # Перечислить все необходимые хосты через пробел.
```
Из корневой директории запустить:
```
docker compose up
```
**По умолчанию проект работает на порту 8000.**

Для создания суперпользователя необходимо запустить комманду:
```
docker exec -it container_id python manage.py createsuperuser
```



Для просмотра swagger документации используйется

http://localhost:8000/api/schema/docs/
