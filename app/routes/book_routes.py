#app\routes\book_routes.py
"""
Модуль для керування книжковим фондом (CRUD).
Реалізує асинхронну взаємодію з PostgreSQL для створення, читання, оновлення та видалення книг.
"""
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..schemas.book_schemas import Book, BookUpdate, BookCreate, BookNotFoundError
from ..database.session import get_db
from ..database.book_models import BookDB
import logging

# Налаштування логера для відстеження операцій у цьому модулі
logger = logging.getLogger("api_logger")
router = APIRouter(prefix="/books", tags=["Книжковий CRUD з Postgres"])


@router.post("/", response_model=Book)
async def create_book(book: BookCreate, db: AsyncSession = Depends(get_db)):
    """
    Створює новий запис про книгу в базі даних.

    - **book**: дані книги (назва, автор, рік) згідно зі схемою BookCreate.
    - **db**: асинхронна сесія бази даних.
    """
    # Конвертуємо Pydantic модель у SQLAlchemy модель
    new_book = BookDB(**book.model_dump())
    db.add(new_book)

    # Синхронізуємо стан з БД для отримання автоматично згенерованого ID
    await db.flush()
    await db.refresh(new_book)

    return new_book

@router.get("/", response_model=list[Book])
async def get_books(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):
    """
    Отримує список усіх книг з підтримкою пагінації.

    - **skip**: кількість записів, які слід пропустити (для пагінації).
    - **limit**: максимальна кількість записів у відповіді.
    """
    result = await db.execute(select(BookDB).offset(skip).limit(limit))
    books = result.scalars().all()
    return books


@router.get("/{book_id}", response_model=Book)
async def get_book(book_id: int, db: AsyncSession = Depends(get_db)):
    """
    Отримує детальну інформацію про конкретну книгу за її ID.

    У разі відсутності книги викликає BookNotFoundError, який обробляється
    кастомним exception handler у main.py.
    """
    result = await db.execute(select(BookDB).where(BookDB.id == book_id))
    book = result.scalar_one_or_none()

    if not book:
        logger.warning(f"Користувач шукав книгу з ID {book_id}, але її немає в базі!") # Логування виклику помилки
        raise BookNotFoundError(book_id=book_id) # Стало: викликаємо наше виключення!

    return book


@router.put("/{book_id}", response_model=Book)
async def update_book(book_id: int, book_update: BookUpdate, db: AsyncSession = Depends(get_db)):
    """
    Частково або повністю оновлює дані існуючої книги.

    - **book_id**: ідентифікатор книги.
    - **book_update**: поля для оновлення (опціональні).
    """
    result = await db.execute(select(BookDB).where(BookDB.id == book_id))
    book = result.scalar_one_or_none()
    if not book:
        raise HTTPException(status_code=404, detail="Книга не знайдена")

    update_data = book_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(book, key, value)

    return book


# 5. Видалення книги (Delete)
@router.delete("/{book_id}")
async def delete_book(book_id: int, db: AsyncSession = Depends(get_db)):
    """
    Видаляє книгу з бази даних за її ідентифікатором.
    """
    result = await db.execute(select(BookDB).where(BookDB.id == book_id))
    book = result.scalar_one_or_none()

    if not book:
        raise BookNotFoundError(book_id=book_id) # Стало

    await db.delete(book)
    return {"message": "Книга успішно видалена"}