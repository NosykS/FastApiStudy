# 🚀 FastApiStudy

Навчальний проєкт для опанування сучасного стеку розробки API на Python. Додаток реалізує систему управління книгами та подіями з повноцінною авторизацією та контейнеризацією.

## 🛠 Технологічний стек
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **Database:** PostgreSQL (Production), SQLite (Testing)
- **ORM:** SQLAlchemy 2.0 (Async) + Alembic
- **Validation:** [Pydantic V2](https://docs.pydantic.dev/) (Settings Management)
- **Security:** JWT (JSON Web Tokens), OAuth2, Passlib (bcrypt)
- **Testing:** [Pytest](https://docs.pytest.org/) + `pytest-asyncio` + `httpx`
- **DevOps:** [Docker](https://www.docker.com/)

## 🌟 Основні можливості
1. **Authentication System**: Реєстрація та логін з видачею токенів (JWT).
2. **CRUD Operations**: Повний асинхронний цикл роботи з книгами у БД.
3. **Smart Testing**: Автоматизовані тести з використанням SQLite `:memory:` для максимальної швидкості.
4. **Environment Isolation**: Надійна система налаштувань через Pydantic-settings та `.env`.
5. **Logging**: Система логування подій у файл `api.log`.

## ⚙️ Налаштування та запуск

### 1. Налаштування середовища
Створіть файл `.env` у корені проєкту. Це обов'язково, оскільки паролі не зберігаються в коді:

```env
SECRET_KEY=ваш_дуже_секретний_ключ
ALGORITHM=HS256
DB_PASSWORD=ваш_пароль_до_postgres
DB_NAME=fastapi_study
```

### 2. Запуск через Docker 🐳 (Рекомендовано)

```Bash
# Збірка та запуск через Docker Desktop
docker build -t fastapi-study-app .
docker run -p 8080:8000 --env-file .env fastapi-study-app
API доступне за адресою: http://localhost:8080/docs
```

### 3. Локальний запуск

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
- app/
  - core/      — налаштування безпеки (JWT, хешування паролів).
  - database/  — моделі SQLAlchemy та логіка підключення до БД.
  - routes/    — API ендпоінти (книги, користувачі, події).
  - schemas/   — Pydantic-моделі для валідації вхідних/вихідних даних.
  - main.py    — головний файл запуску FastAPI додатка.
- test/        — папка з тестами.
  - conftest.py — спільні фікстури (тестова база в пам'яті).
- .env         — файл зі змінними оточення (паролі, ключі).
- pytest.ini   — конфігурація для запуску тестів.

Розроблено NosykS (GitHub: NosykS)