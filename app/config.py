#FastApiStudy\app\config.py
"""
Модуль конфігурації додатка.
Керує налаштуваннями через змінні оточення або файл .env.
"""
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # --- Основні налаштування ---
    app_name: str = "Мій FastAPI-додаток"
    debug: bool = True

    # --- Безпека (JWT) ---
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # --- PostgreSQL ---
    DB_USER: str = "postgres"
    DB_PASSWORD: str
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "fastapi_study"
    DATABASE_URL: Optional[str] = None

    # --- MongoDB ---
    MONGO_URL: str = "mongodb://localhost:27017"
    MONGO_DB_NAME: str = "todo_db"

    # --- Загальний конфіг для Pydantic (один на весь клас) ---
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
