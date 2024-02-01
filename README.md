# picasso_test

## Установка
 - склонировать проект
 - создать виртуальную среду и войдите в неё
```shell
python -m venv venv
source venv/bin/activate
```
 - обновиь pip
```shell
pip install --upgrade pip
```
 - установить необходимые библиотеки из файла зависимостей
```shell
pip install -r requirements.txt
```
 - установить redis
```shell
sudo apt update
sudo apt install redis
```
 - Произвести миграцию
```shell
python manage.py migrate
```

## Запуск сервера
- Запуск Django
```shell
python manage.py runserver
```
 - В отдельном терминале запуск celery worker(для мониторинга событий)
```shell
celery -A picasso_test worker
```