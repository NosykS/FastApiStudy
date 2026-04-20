# Використовуємо офіційний легкий образ Python
FROM python:3.13-slim

# Встановлюємо робочу директорію всередині контейнера
WORKDIR /code

# Копіюємо файл залежностей
COPY requirements.txt .

# Встановлюємо бібліотеки
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь код проекту в контейнер
COPY . .

# Команда для запуску додатка
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]