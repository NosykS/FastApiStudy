#FastApiStudy\app\schemas\event_schemas.py
"""
Модуль Pydantic-схем для управління подіями.
Визначає структури для подій та їх учасників, підтримує аліаси полів
для сумісності з різними форматами JSON.
"""
from pydantic import BaseModel, Field
from datetime import date
from typing import Optional, List


class SchemaParticipant(BaseModel):
    """
    Схема для представлення учасника події.

    Атрибути:
        name (str): Ім'я учасника (2-50 символів).
        email (str): Контактна електронна адреса.
    """
    name: str = Field(..., min_length=2, max_length=50)
    email: str = Field(...)


class EventBase(BaseModel):
    """
    Базова схема події з вкладеним списком учасників.

    Атрибути:
        title (str): Назва події.
        event_date (date): Дата проведення (у JSON використовується аліас 'date').
        location (str): Місце проведення.
        participants (List[SchemaParticipant]): Список учасників, за замовчуванням порожній.
    """
    title: str = Field(..., min_length=1, max_length=100)
    # Alias дозволяє приймати/надсилати "date" у JSON, але використовувати "event_date" у коді Python
    event_date: date = Field(..., alias="date")
    location: str = Field(..., min_length=5, max_length=100)

    # default_factory гарантує, що для кожної нової події буде створено окремий новий список
    participants: List[SchemaParticipant] = Field(default_factory=list)


class EventCreate(EventBase):
    """Схема для створення події. Повністю базується на EventBase."""
    pass


class EventUpdate(BaseModel):
    """
    Схема для часткового оновлення події.
    Всі поля необов'язкові (Optional), що дозволяє оновлювати лише конкретні атрибути.
    """
    title: Optional[str] = None
    event_date: Optional[date] = None
    location: Optional[str] = None
    participants: Optional[List[SchemaParticipant]] = None


class Event(EventBase):
    """
    Схема події для виходу (Response Model). Включає унікальний ID.
    """
    id: int

    model_config = {
        # Дозволяє створювати модель з ORM-об'єктів (наприклад, SQLAlchemy)
        "from_attributes": True,
        # Дозволяє ініціалізувати модель як через 'date' (аліас), так і через 'event_date'
        "populate_by_name": True
    }