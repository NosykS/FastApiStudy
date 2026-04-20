from fastapi.testclient import TestClient
from app.main import app

# Створюємо клієнт для тестування
client = TestClient(app)

def test_read_main():
    """Перевірка доступності головної сторінки"""
    response = client.get("/")
    assert response.status_code == 200
    # Перевіряємо, чи підтягнулася назва з нашого .env
    assert "Супер Додаток від KisoN" in response.json()["message"]
