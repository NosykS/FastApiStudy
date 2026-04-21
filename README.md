# 🚀 FastApiStudy

Навчальний проєкт для опанування сучасного стеку розробки API на Python. Додаток реалізує систему управління книгами та подіями з повноцінною авторизацією та контейнеризацією.

## 🛠 Технологічний стек
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **Database:** PostgreSQL (Production), SQLite (Testing)
- **Migrations** Alembic
- **ORM:** SQLAlchemy 2.0 (Async) 
- **Validation:** [Pydantic V2](https://docs.pydantic.dev/) (Settings Management)
- **Security:** JWT (JSON Web Tokens), OAuth2, Passlib (bcrypt)
- **Testing:** [Pytest](https://docs.pytest.org/) + `pytest-asyncio` + `httpx`
- **DevOps:** [Docker](https://www.docker.com/)


## 🌟 Основні можливості
1. **Authentication System**: Реєстрація та логін з видачею токенів (JWT).
2. **CRUD Operations**: Повний асинхронний цикл роботи з книгами у БД.
3. **Database Migrations**: Версіонування структури БД за допомогою Alembic.
4. **Smart Testing**: Автоматизовані тести з використанням SQLite `:memory:` для максимальної швидкості.
5. **Environment Isolation**: Надійна система налаштувань через Pydantic-settings та `.env`.
6. **Logging**: Система логування подій у файл `api.log`.

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
DATABASE_URL=postgresql+asyncpg://postgres:your_password@localhost:5432/fastapi_study
```
### 2. Міграції бази даних
Перед першим запуском необхідно застосувати міграції, щоб створити таблиці в PostgreSQL:

```Bash
alembic upgrade head
```

### 3. Запуск через Docker 🐳 (Рекомендовано)

```Bash
# Збірка та запуск через Docker Desktop
docker build -t fastapi-study-app .
docker run -p 8080:8000 --env-file .env fastapi-study-app
```
API доступне за адресою: http://localhost:8080/docs

### 4. Локальний запуск

```Bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

🧪 Тестування
Проєкт використовує pytest-asyncio для асинхронних тестів. Тести бази даних автоматично використовують SQLite в пам'яті, тому не потребують запущеного PostgreSQL.

```Bash
# Запуск усіх тестів
pytest

# Запуск з перевіркою покриття (coverage)
pytest --cov=app
```

📂 Структура проєкту
- `app/` — основний код додатка.
  - `core/`      — налаштування безпеки (JWT, хешування паролів).
  - `database/`  — моделі SQLAlchemy та логіка підключення до БД.
  - `routes/`    — API ендпоінти.
  - `schemas/`   — Pydantic-моделі для валідації.
- `alembic/`     — папка з історією міграцій.
- `test/`        — автоматизовані тести.
- `alembic.ini`  — конфігурація Alembic.
- `pytest.ini`   — конфігурація для запуску тестів.

Розроблено [NosykS](https://github.com/NosykS)