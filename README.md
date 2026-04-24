# 🚀 FastApiStudy

Навчальний проєкт для опанування сучасного стеку розробки API на Python. Додаток реалізує систему управління книгами та подіями з повноцінною авторизацією та контейнеризацією.

![CI Status](https://github.com/NosykS/FastApiStudy/actions/workflows/main.yml/badge.svg)

## 🛠 Технологічний стек
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **Database:** PostgreSQL (Production), SQLite (Testing)
- **Migrations** Alembic
- **ORM:** SQLAlchemy 2.0 (Async) 
- **Validation:** [Pydantic V2](https://docs.pydantic.dev/) (Settings Management)
- **Security:** JWT (JSON Web Tokens), OAuth2, Passlib (bcrypt)
- **Testing:** [Pytest](https://docs.pytest.org/) + `pytest-asyncio` + `httpx`
- **DevOps:** [Docker](https://www.docker.com/), GitHub Actions (CI/CD)


## 🌟 Основні можливості
1. **Authentication & Authorization**: Повноцінна система реєстрації та входу з використанням JWT-токенів.
2. **Extended CRUD**: Асинхронна робота з сутностями Books та Events.
3. **Database Migrations**: Автоматичне керування схемою БД через Alembic.
4. **CI/CD Pipeline**: Автоматична перевірка коду та застосування міграцій до бази на Render при кожному пуші в main.
5. **Smart Testing**: Тести використовують SQLite `:memory:`, що дозволяє перевіряти логіку без підключення до основної бази.
6. **Environment Isolation**: Надійна система налаштувань через Pydantic-settings та `.env`.
7. **Logging**: Система логування подій у файл `api.log`.

## ⚙️ Налаштування та запуск

### 1. Налаштування середовища
Створіть файл `.env` у корені проєкту. Це обов'язково, оскільки паролі не зберігаються в коді:

```env
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
DB_USER=postgres
DB_PASSWORD=your_password
DB_NAME=fastapi_study
DB_HOST=localhost
DB_PORT=5432

# URL для асинхронного підключення
DATABASE_URL=postgresql+asyncpg://user:password@host:port/dbname
```
### 2. Міграції бази даних
Проєкт використовує Alembic для версіонування. Для локального оновлення бази:

```Bash
alembic upgrade head
```

### 3. Запуск через Docker 🐳 (Рекомендовано)

```Bash
docker build -t fastapi-study-app .
docker run -p 8080:8000 --env-file .env fastapi-study-app
```
API доступне за адресою: http://localhost:8080/docs

### 4. Локальний запуск

```Bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Документація API буде доступна за адресою: http://localhost:8000/docs

## 🧪 Тестування
Проєкт використовує pytest-asyncio для асинхронних тестів. Тести бази даних автоматично використовують SQLite в пам'яті, тому не потребують запущеного PostgreSQL.

```Bash
# Запуск усіх тестів
pytest

# Запуск з перевіркою покриття (coverage)
pytest --cov=app
```

📂 Структура проєкту
- `app/` — ядро програми.
  - `core/`      — налаштування безпеки (JWT, хешування паролів).
  - `database/`  — моделі SQLAlchemy та логіка підключення до БД.
  - `routes/`    — API ендпоінти.
  - `schemas/`   — Pydantic-моделі для валідації.
- `alembic/`     — скрипти міграцій.
- `test/`        — набір тестів для API та бази даних.
- `alembic.ini`  — конфігурація Alembic.
- `pytest.ini`   — конфігурація для запуску тестів.
- `.github/workflows/` — конфігурація автоматичного деплою міграцій.

Розроблено [NosykS](https://github.com/NosykS)