#FastApiStudy\app\routes\put_routes.py
"""
Модуль для керування даними користувачів.
Реалізує методи PUT для повного оновлення інформації та DELETE для видалення записів,
використовуючи імітовану базу даних у пам'яті (fake_db).
"""
from fastapi import APIRouter, HTTPException, Path
from pydantic import BaseModel, Field

router = APIRouter(prefix="/users", tags=["Керування користувачами"])

# 1. Імітуємо базу даних у пам'яті (in-memory storage)
fake_db = {
    1: {"name": "Анна", "age": 25},
    2: {"name": "Борис", "age": 30},
}


# 2. Модель Pydantic для валідації вхідних даних користувача
class User(BaseModel):
    """
    Схема даних користувача.

    Атрибути:
        name (str): Ім'я (від 2 до 50 символів).
        age (int): Вік (допустимий діапазон від 1 до 120 років).
    """
    name: str = Field(..., min_length=2, max_length=50, description="Ім'я користувача")
    age: int = Field(..., ge=1, le=120, description="Вік користувача (від 1 до 120)")


# 3. Ендпоінт для оновлення користувача
@router.put("/{user_id}", summary="Повне оновлення даних користувача")
async def update_user(user_id: int, updated_data: User):
    """
    Повністю замінює дані існуючого користувача за його ідентифікатором.

    Аргументи:
    - **user_id**: унікальний ID користувача в системі.
    - **updated_data**: об'єкт User з новими даними.

    Повертає оновлений об'єкт або 404 помилку, якщо користувача не знайдено.
    """
    # Перевірка наявності запису в імпровізованій базі
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="Користувача не знайдено!")

    # Конвертація моделі Pydantic у словник для збереження
    fake_db[user_id] = updated_data.model_dump()

    return {
        "message": "Дані користувача успішно оновлено!",
        "updated_user": fake_db[user_id]
    }


# 4. Ендпоінт для видалення користувача
@router.delete("/{user_id}", summary="Видалення користувача")
async def delete_user(
        user_id: int = Path(..., title="ID користувача", description="Унікальний ідентифікатор користувача")
):
    """
    Видаляє запис про користувача з бази даних за вказаним ID.

    Параметри:
    - **user_id**: ідентифікатор, що передається у шляху запиту.

    Використовує клас Path для надання додаткових метаданих у документації OpenAPI.
    """
    # 1. Перевірка існування користувача перед видаленням
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="Користувача не знайдено")

    # 2. Видалення ключа зі словника
    del fake_db[user_id]

    return {"message": f"Користувача з ID {user_id} успішно видалено"}
