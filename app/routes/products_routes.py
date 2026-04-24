#FastApiStudy\app\routes\product_routes.py
"""
Модуль каталогу товарів.
Демонструє складну валідацію Query-параметрів, використання патернів (Regex),
налаштування прикладів відповідей для OpenAPI (Swagger) та роботу зі списками в параметрах запиту.
"""
from fastapi import APIRouter, Query

router = APIRouter(prefix="/products", tags=["Каталог товарів"])

@router.get(
    "/",
    summary="Пошук товарів з фільтрацією",
    description="Дозволяє шукати товари за текстом, пагінацією та напрямком сортування.",
    responses={
        200: {
            "description": "Успішний пошук товарів",
            "content": {
                "application/json": {
                    "example": {
                        "message": "Параметри успішно прийняті!",
                        "search_query": "laptop",
                        "page": 1,
                        "sort_order": "asc"
                    }
                }
            }
        }
    }
)
async def get_products(
    # 1. Обов'язковий параметр (три крапки '...' вказують на обов'язковість)
    query: str = Query(..., min_length=3, description="Текст для пошуку (мін. 3 символи)"),
    # 2. Опціональна пагінація з обмеженням діапазону (Greater than or Equal / Less than or Equal)
    page: int = Query(1, ge=1, le=100,description="Номер сторінки (від 1 до 100)"),
    # 3. Сортування з використанням регулярного виразу (pattern) для обмеження варіантів
    sort: str = Query("asc", pattern="^(asc|desc)$", description="Напрямок сортування: 'asc' або 'desc'")
):
    """
    Виконує пошук товарів на основі заданих фільтрів.

    Повертає підтвердження прийнятих параметрів. Валідація відбувається на рівні FastAPI
    ще до виконання тіла функції.
    """
    return {
        "message": "Параметри успішно прийняті!",
        "search_query": query,
        "page": page,
        "sort_order": sort
    }

# 4. Списки в Query-параметрах
@router.get(
    "/tags",
    summary="Фільтрація за тегами",
    responses={
        200: {
            "description": "Список обраних тегів",
            "content":{
                "application/json": {
                    "example": {
                        "selected_tags": ["electronics", "sale"]
                    }
                }
            }
        }
    }
)
async def get_tags(tags: list[str] = Query(None, description="Список тегів (можна вказати кілька)")):
    """
    Демонструє отримання списку значень з одного параметра запиту.

    Приклад запиту: `/products/tags?tags=electronics&tags=sale`
    """
    return {
        "selected_tags": tags if tags else "Не обрано жодних тегів"
    }
