#FastApiStudy\clean_db.py
"""
Скрипт для видалення бази даних
"""

# import asyncio
# from sqlalchemy.ext.asyncio import create_async_engine
# from sqlalchemy import text
# from app.config import settings
#
#
# async def clean():
#     # Використовуємо твій DATABASE_URL з .env
#     engine = create_async_engine(settings.DATABASE_URL)
#
#     async with engine.begin() as conn:
#         print("Очищення бази даних...")
#         # Видаляємо таблиці, які заважають
#         await conn.execute(text("DROP TABLE IF EXISTS books CASCADE;"))
#         await conn.execute(text("DROP TABLE IF EXISTS alembic_version;"))
#         print("Готово! Таблиці видалено.")
#
#
# if __name__ == "__main__":
#     asyncio.run(clean())