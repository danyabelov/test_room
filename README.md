# Подготовка и запуск проекта
Склонируйте репозиторий

```bash
git clone https://github.com/danyabelov/test_room.git
```
## Подготовка базы данных PostgreSQL
Для работы необходима версия PostgreSQL 16.

Запустите PostgreSQL и создайте БД "rooms"

## Настройка виртуального окружения и проведение миграций
В корне проекта создайте виртуальную среду

```bash
python -m venv .venv
```

Активируйте среду

```bash
 ./.venv/scripts/activate
```

Установите необходимые библиотеки

```bash
pip install -r requirements.txt
```

Также необходимо заполнить .env файл по образцу ниже

```
DB_ENGINE=django.db.backends.postgresql_psycopg2
DB_NAME=<DB_NAME>
POSTGRES_USER=<POSTGRES_USER>
POSTGRES_PASSWORD=<POSTGRES_PASSWORD>
DB_HOST=127.0.0.1
DB_PORT=5432
SECRET_KEY=<SECRET_KEY>
DEBUG=True
```

Проведите миграции проекта
```bash
python manage.py makemigrations
python manage.py migrate
```

Запуск проекта
```bash
python manage.py runserver
```
Для админ-панели создание суперюзера
```bash
python manage.py createsuperuser
```
