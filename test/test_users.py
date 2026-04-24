#FastApiStudy\test\test_users.py
import pytest
from fastapi.testclient import TestClient
from jose import jwt
from datetime import datetime, timedelta, timezone
from app.main import app
from app.config import settings

client = TestClient(app)

# 1. Фікстура для отримання токена адміністратора
@pytest.fixture
def admin_token():
    payload = {
        "sub": "admin_user",
        "role": "admin",
        "exp": datetime.now(timezone.utc) + timedelta(minutes=15)
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return token

# 2. Тест публічного ендпоінту (Головна)
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Ласкаво просимо" in response.json()["message"]

# 3. Тест захищеного ендпоінту (Admin Only)
def test_admin_access_denied_without_token():
    response = client.get("/admin-only")
    assert response.status_code == 401 # Unauthorized

def test_admin_access_granted_with_token(admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = client.get("/admin-only", headers=headers)
    assert response.status_code == 200
    assert "Вітаю, Адміне" in response.json()["message"]

# 4. Тест валідації (Створення товару з помилкою)
def test_create_item_invalid_data():
    payload = {"name": "X", "price": -10} # Надто коротке ім'я і від'ємна ціна
    response = client.post("/items/", json=payload)
    assert response.status_code == 422 # Unprocessable Entity
