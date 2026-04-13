#app\core\security.py
"""
Модуль для забезпечення безпеки: хешування паролів та робота з JWT-токенами.
"""
import secrets
import string
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from app.config import settings

# Налаштування контексту для хешування паролів (алгоритм bcrypt)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """Генерує безпечний хеш пароля (обрізка до 72 символів для сумісності з bcrypt)."""
    return pwd_context.hash(password[:72])

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Перевіряє відповідність відкритого пароля його збереженому хешу."""
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    """Створює JWT access_token з даними користувача та терміном дії."""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def generate_random_token(length: int = 20):
    """Генерує випадковий рядок (refresh_token) заданої довжини."""
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))
