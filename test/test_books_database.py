#FastApiStudy\test\test_books_database.py
import pytest
from sqlalchemy import select
from app.database.book_models import BookDB


@pytest.mark.asyncio
async def test_create_and_read_book(db_session):
    # 1. CREATE: Створюємо книгу з JSON-даними
    new_book = BookDB(
        title="Тестова Книга",
        author="Автор Тест",
        year=2024,
        extra_data={"test": "passed"}
    )
    db_session.add(new_book)
    await db_session.commit()

    # 2. READ: Перевіряємо, чи вона є в базі
    result = await db_session.execute(select(BookDB).filter_by(title="Тестова Книга"))
    book_from_db = result.scalar_one()

    assert book_from_db.author == "Автор Тест"
    assert book_from_db.extra_data["test"] == "passed"