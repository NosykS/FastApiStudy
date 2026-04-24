#FastApiStudy\app\database\session.py
"""
Налаштування підключення до PostgreSQL через асинхронний драйвер asyncpg.
"""
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from app.config import settings

# 1. Формуємо базовий URL підключення
if settings.DATABASE_URL:
    # Якщо в .env вказано повний рядок (наприклад, для Render)
    db_url = settings.DATABASE_URL
else:
    # Якщо вказані окремі змінні (локально або в Docker-compose)
    db_url = (
        f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@"
        f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
    )

# 2. Автоматична обробка SSL для Render
# Якщо в адресі є 'render.com', але немає параметра ssl — додаємо його
if "render.com" in db_url and "ssl=" not in db_url:
    separator = "&" if "?" in db_url else "?"
    db_url += f"{separator}ssl=require"

# 3. Створення двигуна (Engine)
# pool_pre_ping=True допомагає уникати помилок при розриві з'єднання базою
engine = create_async_engine(
    db_url,
    echo=settings.debug,
    pool_pre_ping=True
)

# Фабрика сесій
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Базовий клас для моделей
Base = declarative_base()

async def get_db():
    """
    Dependency для FastAPI.
    Гарантує відкриття сесії, коміт при успіху та автоматичне закриття.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()