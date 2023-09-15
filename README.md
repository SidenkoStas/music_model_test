# Используемый стек технологий.
- Python
- Django
- Django Rest Framework
- Swagger
- Docker
- Docker compose

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
