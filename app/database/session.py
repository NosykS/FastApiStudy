#app\database\session.py
"""
Налаштування підключення до PostgreSQL через асинхронний драйвер asyncpg.
"""
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
# Імпортуємо ваші налаштування
from app.config import settings

# Збираємо URL динамічно (або беремо готовий, якщо ви додасте його в Settings)
# Але поки що зробимо так, щоб він використовував DB_HOST з налаштувань
DATABASE_URL = (
    f"postgresql+asyncpg://postgres:774456@"
    f"{settings.DB_HOST if hasattr(settings, 'DB_HOST') else 'localhost'}:"
    f"5432/fastapi_study"
)

# Створення двигуна
engine = create_async_engine(DATABASE_URL, echo=True)

# Фабрика сесій для створення з'єднань
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()

async def get_db():
    """Dependency для отримання сесії БД. Автоматично закриває з'єднання після запиту."""
    async with AsyncSessionLocal() as session:
        yield session
        await session.commit()