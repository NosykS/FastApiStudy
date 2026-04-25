# 🚀 FastApiStudy

Навчальний проєкт для опанування сучасного стеку розробки API на Python. Додаток реалізує систему управління книгами та подіями з повноцінною авторизацією та контейнеризацією.

![CI Status](https://github.com/NosykS/FastApiStudy/actions/workflows/main.yml/badge.svg)

## 🛠 Технологічний стек
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Databases**:
  - **PostgreSQL** (SQLAlchemy 2.0 Async) — для книг та користувачів.
  - **MongoDB** (Motor/PyMongo) — для асинхронної роботи з To-Do задачами.
  - **SQLite** — для швидкого асинхронного тестування.
- **Migrations** Alembic (для PostgreSQL).
- **ORM/ODM**: SQLAlchemy 2.0 (SQL), Motor (NoSQL). 
- **Validation:** [Pydantic V2](https://docs.pydantic.dev/) (Settings Management)
- **Security:** JWT (JSON Web Tokens), OAuth2, Passlib (bcrypt)
- **Testing:** [Pytest](https://docs.pytest.org/) + `pytest-asyncio` + `httpx`
- **DevOps**: [Docker](https://www.docker.com/), Docker Compose, GitHub Actions (CI/CD).


## 🌟 Основні можливості
1. **Multi-Database Support**: Паралельна робота з реляційною (PostgreSQL) та NoSQL (MongoDB) базами.
2. **Authentication & Authorization**: Система реєстрації та входу з використанням JWT-токенів.
3. **Extended CRUD**: Асинхронна робота з сутностями Books, Events та To-Do.
4. **Database Migrations**: Автоматичне керування схемою PostgreSQL через Alembic.
5. **CI/CD Pipeline**: Автоматична перевірка коду та деплой міграцій при кожному пуші в `main`.
6. **Smart Testing**: Використання SQLite `:memory:` для миттєвого тестування логіки.
7. **Environment Isolation**: Керування конфігурацією через Pydantic-settings та `.env`.
8. **Logging**: Реєстрація подій у файл `api.log`.

## ⚙️ Налаштування та запуск

### 1. Налаштування середовища
Це обов'язковий крок, оскільки конфіденційні дані не зберігаються в коді. Скопіюйте шаблон та заповніть його:

```Bash
cp .env.example .env
```
Відкрийте .env та замініть your_password, your_secret_key_here та інші значення на ваші власні.

Приклад вмісту .env:

```env
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256

# PostgreSQL
DB_USER=postgres
DB_PASSWORD=your_password
DB_NAME=fastapi_study
DB_HOST=localhost # або 'db' при використанні Docker
DB_PORT=5432
DATABASE_URL=postgresql+asyncpg://user:password@host:port/dbname

# MongoDB
MONGO_URL=mongodb://mongodb_container:27017
MONGO_DB_NAME=todo_db
```
### 2. Запуск через Docker Compose 🐳 (Рекомендовано)
Ця команда автоматично запустить додаток та обидві бази даних:

```Bash
docker-compose up --build
```
- API (Swagger): http://localhost:8080/docs
- MongoDB: доступна внутрішньо для додатка на порті 27017.

### 3. Локальний запуск (без Docker)
Встановіть залежності:

```Bash
pip install -r requirements.txt
```

#### 1. Виконайте міграції PostgreSQL:

```Bash
alembic upgrade head
```

#### 2. Запустіть сервер:

```Bash
uvicorn app.main:app --reload
```
Документація буде доступна за адресою: http://localhost:8000/docs

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
- `docker-compose.yml` — оркестрація контейнерів.

Розроблено [NosykS](https://github.com/NosykS)