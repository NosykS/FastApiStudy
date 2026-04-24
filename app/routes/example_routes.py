#FastApiStudy\app\routes\example_routes.py
"""
Модуль системних прикладів.
Містить демонстраційні ендпоінти для вивчення базових функцій FastAPI,
таких як параметри запиту (Query parameters) та їх валідація.
"""
from fastapi import APIRouter, Query

router = APIRouter(tags=["Системні"])

@router.get("/greet/", summary="Персоналізоване привітання")
async def greet_user(
    name: str = Query(
        "гість",
        max_length=10,
        description="Ім'я користувача для привітання (макс. 10 символів)"
    )
):
    """
    Генерує вітальне повідомлення для користувача.

    Параметри:
    - **name** (str): Ім'я, яке буде додано до привітання.
      - Має значення за замовчуванням: "гість".
      - Обмеження: не більше 10 символів.

    Повертає JSON з привітанням. Якщо довжина імені перевищена, FastAPI
    автоматично поверне 422 Unprocessable Entity.
    """
    return{"message": f"Привіт, {name}!"}
