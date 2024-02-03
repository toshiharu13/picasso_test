# Тестовый API сервер
Данный сервер в тестовом режиме загружает файлы и выдаёт информацию о загруженых файлах.

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
![Celery Badge](https://img.shields.io/badge/Celery-37814A?logo=celery&logoColor=fff&style=flat-square)

## Установка
 - Скачайте код
 - Создайте и активируйте виртуальное окружение
```shell
python -m venv env && source env/bin/activate
```
 - Обновите pip
```shell
pip install --upgrade pip
```
 - Установите необходимые библиотеки из файла зависимостей
```shell
pip install -r requirements.txt
```
 - Установите redis
```shell
sudo apt update 
sudo apt install redis
```
 - Примените миграции
```shell
python manage.py migrate
```
 - Создайте учётную запись администратора командой:
```shell
python manage.py createsuperuser
```
## Запуск сервера
- Запуск Django
```shell
python manage.py runserver
```
 - Убедитесь, что redis сервер запущен, если нет, запустите его в отдельглм окне
```shell
redis-server
```
 - В отдельном терминале запустите celery worker
```shell
celery -A picasso_test worker
```
## Запуск сервера через docker
 - Убедитесь, что у вас установлен docker + docker-compose. Установите в случае отсутствия, к примеру Docker Desktop
```html
https://docs.docker.com/desktop/
```
 - Запустите контейнеры:
```shell
docker-compose up
```

## API ручки
 - api/v1/upload/, запросы - POST, обязательное поле - file
 - api/v1/files/, запросы - GET, обязательный параметр - show_list(True/False)