# Процессы и инструменты управления данными — рабочий репозиторий

Учебный репозиторий курса. Группа ВМО-42.

## Структура
- `docker-compose.yml` — PostgreSQL + pgAdmin
- `requirements.txt` — зависимости Python
- `sql/` — DDL-скрипты и запросы по неделям
- `scripts/` — Python-скрипты (ETL, генерация данных, проверки)
- `docs/` — отчёты и документы по лабораторным работам

## Как запустить окружение
1. `docker compose up -d`
2. `python3 -m venv venv && source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `python scripts/test_connection.py`

## Автор
Федосеев Никита,ВМО-42
