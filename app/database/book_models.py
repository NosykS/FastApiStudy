#app\database\book_models.py
"""
Модуль опису SQLAlchemy-моделей для книжкового сховища.
Визначає структуру таблиць у базі даних PostgreSQL.
"""
from sqlalchemy import Column, Integer, String
from app.database.session import Base

class BookDB(Base):
    """
    SQLAlchemy модель для таблиці 'books'.

    Атрибути:
        id (int): Унікальний ідентифікатор книги (Primary Key).
        title (str): Назва книги.
        author (str): Прізвище та ім'я автора.
        year (int): Рік видання книги.
    """
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True) # Первинний ключ з індексацією для швидкого пошуку
    title = Column(String, nullable=False) # Назва книги, обов'язкове поле
    author = Column(String, nullable=False) # Автор книги, обов'язкове поле
    year = Column(Integer, nullable=False) # Рік видання, обов'язкове поле
