# 🚀 FastApiStudy

Навчальний проєкт для опанування сучасного стеку розробки API на Python. Додаток реалізує систему управління книгами та подіями з повноцінною авторизацією.

## 🛠 Технологічний стек
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **Database:** PostgreSQL (асинхронне підключення через SQLAlchemy + asyncpg)
- **Security:** JWT (JSON Web Tokens), Passlib (bcrypt), OAuth2
- **Validation:** Pydantic v2
- **Logging:** Вбудована система логування у файл `api.log`

## 🌟 Основні можливості
1. **Authentication System**: Реєстрація та логін з видачею Access та Refresh токенів.
2. **Role-Based Access Control (RBAC)**: Обмеження доступу до адмін-функцій (наприклад, `/admin-only`).
3. **Book CRUD**: Повний цикл роботи з книгами (створення, читання, оновлення, видалення) у БД.
4. **Events API**: Система управління подіями зі складними моделями даних.
5. **Custom Middleware**: Обробка 500-х помилок та кастомні Exception Handlers.
6. **Async Support**: Повністю асинхронна архітектура для високої продуктивності.

## 📂 Структура проєкту
- `app/main.py` — Точка входу, налаштування Middleware та роутерів.
- `app/core/` — Логіка безпеки та конфігурація.
- `app/database/` — Моделі SQLAlchemy та налаштування сесій.
- `app/routes/` — Контролери (ендпоінти) розділені за функціоналом.
- `app/schemas/` — Pydantic моделі для валідації запитів та відповідей.

## 🚀 Запуск проєкту
1. Створіть віртуальне оточення та встановіть залежності:
   ```bash
   pip install -r requirements.txt
2. Налаштуйте файл .env (використовуйте config.py як зразок).

3. Запустіть сервер: 
    ```bash
    uvicorn app.main:app --reload

4. Документація доступна за адресою: http://127.0.0.1:8000/docs