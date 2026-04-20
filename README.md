# 🚀 FastApiStudy

Навчальний проєкт для опанування сучасного стеку розробки API на Python. Додаток реалізує систему управління книгами та подіями з повноцінною авторизацією та контейнеризацією.

## 🛠 Технологічний стек
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **Database:** PostgreSQL (SQLAlchemy + asyncpg)
- **Validation & Settings:** [Pydantic V2](https://docs.pydantic.dev/) (Settings Management)
- **Security:** JWT (JSON Web Tokens), OAuth2, Passlib (bcrypt)
- **Testing:** [Pytest](https://docs.pytest.org/) & [Pytest-cov](https://pytest-cov.readthedocs.io/)
- **DevOps:** [Docker](https://www.docker.com/)

## 🌟 Основні можливості
1. **Authentication System**: Реєстрація та логін з видачею токенів.
2. **CRUD Operations**: Повний асинхронний цикл роботи з книгами у БД.
3. **Automated Testing**: Покриття тестів та генерація звітів про покриття коду.
4. **Containerization**: Готовий Docker-образ для швидкого розгортання.
5. **Logging**: Система логування у файл `api.log`.

## ⚙️ Налаштування та запуск

### 1. Налаштування середовища
Створіть файл `.env` у корені проєкту (використовуйте `app/config.py` як орієнтир):
```env
SECRET_KEY=your_secret_key
DEBUG=True
DB_HOST=localhost # або host.docker.internal для Docker
```

### 2. Запуск через Docker 🐳 (Рекомендовано)
```Bash
# Збірка образу
docker build -t fastapi-study-app .

# Запуск контейнера
docker run -p 8080:8000 --env-file .env fastapi-study-app
```
API буде доступне за адресою: http://localhost:8080/docs

### 3. Локальний запуск
```Bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

🧪 Тестування
Для запуску тестів та перевірки покриття коду виконайте:

```Bash
python -m pytest --cov=app
```

## 📂 Структура проєкту
- app/core/ — Конфігурація та безпека.
- app/database/ — Асинхронні сесії та моделі SQLAlchemy.
- app/routes/ — Ендпоінти, розділені за модулями.
- test/ — Автоматизовані тести.
- Dockerfile — Налаштування для створення контейнера.

Розроблено NosykS (GitHub: NosykS)
