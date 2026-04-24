#FastApiStudy\app\routes\auth_routes.py
"""
Модуль для керування процесами аутентифікації.
Забезпечує перевірку облікових даних користувача та генерацію токенів доступу (JWT).
"""
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.core import security

router = APIRouter(prefix="/auth", tags=["Аутентифікація"])

# Тимчасова база (потім перенесемо в PostgreSQL)
users_db = {
    "admin_user": {
        "username": "admin_user",
        "hashed_password": security.get_password_hash("admin123"),
        "role": "admin"
    }
}


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Виконує вхід користувача в систему.

    - **username**: логін користувача (передається через OAuth2 форму)
    - **password**: пароль користувача

    Повертає об'єкт з access_token, refresh_token та типом токена.
    Викидає HTTPException 401 при невірних даних.
    """
    # Пошук користувача в імпровізованій базі
    user = users_db.get(form_data.username)

    # Валідація існування користувача та перевірка пароля через хеш
    if not user or not security.verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Невірний логін або пароль")

    # Створення JWT-токена з корисним навантаженням (ім'я та роль)
    access_token = security.create_access_token(
        data={"sub": user["username"], "role": user["role"]}
    )
    # Генерація унікального refresh токена довжиною 20 символів
    refresh_token = security.generate_random_token(20)

    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}