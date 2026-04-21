#test\test_books_api.py
import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app
from app.database.session import get_db


# 1. Створюємо "підміну" для залежності get_db
# Ця функція буде віддавати ту саму сесію, що і наша фікстура
@pytest.mark.asyncio
async def test_create_book_via_api(db_session):
    # Dependency override: змушуємо FastAPI використовувати тестову сесію
    async def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    # 2. Використовуємо AsyncClient для виклику ендпоінтів
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        payload = {
            "title": "API Тест Книга",
            "author": "Python Developer",
            "year": 2026,
            "extra_data": {"status": "tested"}
        }

        response = await ac.post("/books/", json=payload)

    # 3. Перевірки (Assertions)
    assert response.status_code == 200  # Або 201, якщо ти налаштував статус
    data = response.json()
    assert data["title"] == "API Тест Книга"
    assert "id" in data  # Перевіряємо, що база присвоїла ID

    # Чистимо підміни після тесту
    app.dependency_overrides.clear()
