Инструкция для запуска.

Из корневой директории запустить: docker compose up
Работает на порту 8000.

Для создания создания суперпользователя:
docker exec -it container_id python manage.py createsuperuser

Для просмотра swagger документации используйется url "http://localhost:8000/api/schema/docs/"
