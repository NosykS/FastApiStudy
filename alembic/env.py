import asyncio
from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import async_engine_from_config
from alembic import context

# Імпорт твоїх налаштувань та моделей
from app.config import settings
from app.database.session import Base
from app.database.book_models import BookDB  # Важливо для autogenerate

# Об'єкт конфігурації Alembic
config = context.config

# Налаштування логування
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Вказуємо метадані моделей
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Запуск міграцій в 'offline' режимі (генерує SQL скрипт)"""
    url = settings.DATABASE_URL # Використовуємо наш URL навіть тут
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def do_run_migrations(connection):
    """Синхронний помічник для виконання міграцій"""
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online() -> None:
    """Запуск міграцій в асинхронному режимі (Online)"""
    configuration = config.get_section(config.config_ini_section, {})
    configuration["sqlalchemy.url"] = settings.DATABASE_URL

    connectable = async_engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()

# Цей блок має бути ПОЗА функціями
if context.is_offline_mode():
    run_migrations_offline()
else:
    try:
        asyncio.run(run_migrations_online())
    except (KeyboardInterrupt, SystemExit):
        pass