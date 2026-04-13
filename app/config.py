#app\config.py
"""
Модуль конфігурації додатка.
Використовує pydantic-settings для керування налаштуваннями через змінні оточення
або файл .env. Містить ключі безпеки та глобальні параметри сервера.
"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Клас налаштувань додатка.

    Атрибути:
        app_name (str): Назва проекту, що відображається в документації.
        debug (bool): Режим розробки (True для детальних помилок).
        SECRET_KEY (str): Секретний ключ для підпису JWT-токенів (тримати в таємниці!).
        ALGORITHM (str): Алгоритм шифрування JWT (за замовчуванням HS256).
        ACCESS_TOKEN_EXPIRE_MINUTES (int): Час життя токена доступу в хвилинах.
    """
    # Основні налаштування
    app_name: str = "Мій FastAPI-додаток"
    debug: bool = True

    # Налаштування безпеки (JWT)
    # У реальному проекті ці значення мають завантажуватися з .env файлу
    SECRET_KEY: str = "super-secret-key-12345"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        """Налаштування Pydantic для завантаження даних з файлу .env."""
        env_file = ".env"


# Ініціалізація об'єкта налаштувань для використання в інших модулях
settings = Settings()