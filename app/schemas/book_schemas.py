#app\schemas\book_schemas.py
"""
Модуль Pydantic-схем для валідації даних книг.
Визначає структури вхідних та вихідних даних, а також правила їх перевірки.
"""
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Dict, Any
from datetime import datetime

# Отримуємо поточний рік для динамічної валідації поля 'year'
current_year = datetime.now().year

class BookBase(BaseModel):
    """
    Базова схема книги з загальними полями та правилами валідації.

    Атрибути:
        title (str): Назва (1-100 символів).
        author (str): Автор (2-50 символів).
        year (int): Рік видання (від 0 до поточного року).
    """
    title: str = Field(..., min_length=1, max_length=100, examples=["Кобзар"])
    author: str = Field(..., min_length=2, max_length=50, examples=["Тарас Шевченко"])
    year: int = Field(..., ge=0, le=current_year, examples=[1840])
    extra_data: Optional[Dict[str, Any]] = Field(default={}, examples=[{"genre": "Classic"}])

class BookCreate(BookBase):
    """Схема для створення нової книги. Успадковує всі поля від BookBase."""
    pass

# Схема для відображення
class Book(BookBase):
    """
    Схема для відображення книги в API (включає ID).

    Config:
        from_attributes = True: дозволяє Pydantic працювати з об'єктами SQLAlchemy (ORM).
    """
    id: int
    model_config = ConfigDict(from_attributes=True)

class BookUpdate(BaseModel):
    """
    Схема для часткового оновлення даних книги.
    Всі поля є опціональними, але якщо вони передані — проходять стандартну валідацію.
    """
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    author: Optional[str] = Field(None, min_length=2, max_length=50)
    year: Optional[int] = Field(None, ge=0, le=current_year)
    extra_data: Optional[Dict[str, Any]] = None

class BookNotFoundError(Exception):
    """
    Кастомний клас виключення для випадків, коли книга не знайдена в БД.

    Args:
        book_id (int): ID книги, яку не вдалося знайти.
    """
    def __init__(self, book_id: int):
        self.book_id = book_id