#app\routes\post_routes.py
"""
Модуль для створення товарів через POST-запити.
Демонструє використання Pydantic-моделей для валідації тіла запиту (Request Body)
та масове створення об'єктів через списки.
"""
from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(prefix="/items", tags=["Створення товарів (POST)"])

# 1. Визначаємо схему даних (модель Pydantic)
class Item(BaseModel):
    """
    Схема даних для товару.

    Атрибути:
        name (str): Назва товару (від 3 до 50 символів).
        price (float): Ціна товару (має бути більше 0).
        is_offer (bool): Прапорець, чи є товар акційним (за замовчуванням False).
    """
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Назва товару (мінімум 3 символи, максимум 50)"
    )
    price: float = Field(
    0.0,
    gt=0,
    description="Ціна товару (має бути строго більше за 0)"
    )
    is_offer: bool = Field(
        default=False,
        description="Чи є товар Вкційним"
    )

# 2. Ендпоінт для створення одного товару
@router.post("/", summary="Створити один товар")
async  def create_item(item: Item):
    """
    Приймає JSON-об'єкт товару та імітує його збереження.

    FastAPI автоматично перевірить вхідні дані на відповідність схемі Item.
    """
    return {
        "message": "Товар успішно створено!",
        "item": item
    }

# 3. Ендпоінт для масового створення (передача масиву JSON)
@router.post("/bulk/", summary="асове створити товарів")
async def create_items(items: list[Item]):
    """
    Приймає список (масив) JSON-об'єктів для одночасного створення декількох товарів.

    - **items**: Список об'єктів, кожен з яких проходить валідацію через модель Item.
    """
    return {
        "message": f"Успішно створено {len(items)} товарів!",
        "items": items
    }
