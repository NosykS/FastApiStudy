#FastApiStudy\app\routes\event_routes.py
"""
Модуль для керування подіями.
Використовує імпровізоване сховище в пам'яті (in-memory storage) для демонстрації
роботи зі складними Pydantic-схемами та аліасами полів.
"""
from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import event_schemas

router = APIRouter(prefix="/events", tags=["Управління подіями"])

# Тимчасове сховище для подій у пам'яті сервера
event_storage = []

@router.get("/", response_model=List[event_schemas.Event])
async def get_events():
    """
    Повертає повний список усіх зареєстрованих подій.
    """
    return event_storage

@router.post("/", response_model=event_schemas.Event, status_code=201)
async def create_event(payload: event_schemas.EventCreate):
    """
    Реєструє нову подію в системі.

    - **payload**: дані події (назва, дата, місце проведення, список учасників).

    Особливість: використовує `by_alias=True`, щоб коректно обробити поле 'date',
    яке в моделі визначено як 'event_date' з аліасом.
    """
    # .model_dump(by_alias=True) перетворює Pydantic-модель у словник,
    # зберігаючи назви ключів, які очікує клієнт (наприклад, "date" замість "event_date")
    new_event = payload.model_dump(by_alias=True)

    # Генерація простого ID на основі поточної довжини списку
    new_event["id"] = len(event_storage)
    event_storage.append(new_event)

    return new_event
