#FastApiStudy\app\schemas\todo_schemas.py
from pydantic import BaseModel, Field
from typing import Optional

class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    is_completed: bool = False

class TodoResponse(TodoCreate):
    id: str = Field(alias="_id") # MongoDB повертає _id

    class Config:
        populate_by_name = True # Дозволяє використовувати id замість _id при створенні об'єкта