#app\routes\async_routes.py
"""
Модуль для демонстрації асинхронних можливостей FastAPI.
Містить приклади неблокуючих операцій, роботу з зовнішніми API та паралельне виконання задач.
"""
import asyncio
from time import sleep

import httpx
from fastapi import APIRouter


router = APIRouter(prefix="/async-demo", tags=["Асинхронність"])

# 1. Простий асинхронний ендпоінт
@router.get("/hello", summary="Просте привітання")
async def say_hello():
    """
    Повертає просте текстове повідомлення.
    Використовується для перевірки базової працездатності асинхронного роутера.
    """
    return {"message": "Привіт,асинхронний світ!"}

# 2. Імітація довгої операції
@router.get("/long-task", summary="Імітація довгої задачі")
async def long_task():
    """
    Імітує виконання тривалої операції (наприклад, обробка відео або складні розрахунки).
    Використовує asyncio.sleep, щоб не блокувати потік виконання інших запитів.
    """
    await asyncio.sleep(5) # Очікуємо 5 секунд без блокування сервера
    return {"message": "Готово! Я почекав 5 секунд."}

# 3. Одиночний запит до зовнішнього API
@router.get("/external-api", summary="Запит до зовнішнього API")
async def get_external_api():
    """
    Виконує асинхронний HTTP-запит до стороннього ресурсу за допомогою бібліотеки httpx.
    """
    url = "https://jsonplaceholder.typicode.com/post/1"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return {"external_data": response.json()}

# 4. Паралельні запити через asyncio.gather
async def fetch_url(url: str, client: httpx.AsyncClient):
    """
    Утилітарна функція для отримання JSON-даних за вказаною URL-адресою.

    Args:
        url (str): Адреса ресурсу.
        client (httpx.AsyncClient): Асинхронний клієнт для виконання запиту.
    """
    response = await client.get(url)
    return response.json()

@router.get("/parallel-requests", summary="Паралельні запити")
async def parallel_requests():
    """
    Демонструє конкурентне виконання декількох HTTP-запитів одночасно.
    Використовує asyncio.gather для очікування завершення всіх задач у списку.
    """
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1"
        "https://jsonplaceholder.typicode.com/posts/2"
    ]

    async with httpx.AsyncClient() as client:
        # Запускаємо обидва запити одночасно
        tasks = [fetch_url(url, client) for url in urls]
        responses = await asyncio.gather(*tasks)
    return{"result": responses}
