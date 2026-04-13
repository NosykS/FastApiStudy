#app\main.py
"""
Головний модуль додатка FastAPI.
Тут ініціалізується сервер, налаштовується логування, підключаються маршрути (routers),
впроваджується Middleware та обробники помилок (exception handlers).
"""
from fastapi import FastAPI, Request, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from app.config import settings
from app.routes import example_routes, math_routes, products_routes, async_routes, post_routes, put_routes, book_routes, event_routes
from app.database.session import engine, Base
from contextlib import asynccontextmanager
from app.schemas.book_schemas import BookNotFoundError
from starlette.middleware.base import BaseHTTPMiddleware
import logging
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from app.routes import auth_routes

# 0. Конфігурація системи логування
# Записує події у файл api.log та виводить їх у термінал
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s",
    handlers=[
        logging.FileHandler("api.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("api_logger")

# Схема OAuth2 для отримання токена з заголовка 'Authorization: Bearer <token>'
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Dependency для перевірки JWT-токена та ідентифікації користувача.

    Декодує токен, перевіряє його валідність та повертає дані про користувача (sub та role).
    Викидає HTTPException 401, якщо токен недійсний.
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        role: str = payload.get("role")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Невалідний токен"
            )
        return {"username": username, "role": role}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Помилка валідації токена"
        )

def require_role(required_role: str):
    """
    Фабрика залежностей для перевірки прав доступу (RBAC).

    Args:
        required_role (str): Роль, необхідна для доступу до маршруту (наприклад, 'admin').
    """
    def role_checker(current_user: dict = Depends(get_current_user)):
        if current_user["role"] != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Недостатньо прав доступу"
            )
        return current_user
    return Depends(role_checker)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Керує життєвим циклом додатка.
    При запуску сервера автоматично створює всі таблиці в базі даних, якщо вони ще не існують.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

# Ініціалізація додатка з налаштуваннями з config.py та логікою lifespan
app = FastAPI(title=settings.app_name, lifespan=lifespan)

@app.exception_handler(BookNotFoundError)
async def book_not_found_handler(request: Request, exc: BookNotFoundError):
    """Обробник кастомної помилки BookNotFoundError: повертає 404 статус та посилання на документацію."""
    return JSONResponse(
        status_code=404,
        content={
            "detail": f"Книгу з ID {exc.book_id} не знайдено в базі даних!",
            "documentation_url": "http://127.0.0.1:8000/docs"
        }
    )

@app.get("/", summary="Головна сторінка", tags=["Системні"])
async def root():
    """Вітальний ендпоінт головної сторінки."""
    return {"message": f"Ласкаво просимо в {settings.app_name}!"}

class CustomErrorMiddleware(BaseHTTPMiddleware):
    """
    Middleware для глобального перехоплення непередбачуваних помилок (500 Internal Server Error).
    Логує виключення та повертає структурований JSON клієнту.
    """
    async def dispatch(self, request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as exc:
            logger.error(f"Критична помилка сервера: {str(exc)}", exc_info=True)
            return JSONResponse(
                status_code=500,
                content={
                    "detail": "На сервері сталася непередбачувана помилка. Наші розробники вже працюють над цим!",
                    "error": str(exc)
                }
            )

# Реєстрація Middleware
app.add_middleware(CustomErrorMiddleware)

# Підключення всіх функціональних роутерів
app.include_router(example_routes.router)
app.include_router(math_routes.router)
app.include_router(products_routes.router)
app.include_router(async_routes.router)
app.include_router(post_routes.router)
app.include_router(put_routes.router)
app.include_router(book_routes.router)
app.include_router(event_routes.router)
app.include_router(auth_routes.router)

@app.get("/admin-only", tags=["Системні"], dependencies=[require_role("admin")])
async def admin_route():
    """Захищений маршрут, доступний тільки для користувачів з роллю 'admin'."""
    return {"message": "Вітаю, Адміне! Цей шлях захищено JWT та роллю."}