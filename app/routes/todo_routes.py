#FastApiStudy\app\routes\todo_routes.py
from fastapi import APIRouter, HTTPException
from bson import ObjectId
from app.schemas.todo_schemas import TodoCreate, TodoResponse
from app.database.mongodb import todo_collection

router = APIRouter()

def serialize_todo(todo) -> dict:
    todo["_id"] = str(todo["_id"])
    return todo

@router.post("/", response_model=TodoResponse)
async def create_task(todo: TodoCreate):
    new_task = todo.model_dump()
    result = await todo_collection.insert_one(new_task)
    created_task = await todo_collection.find_one({"_id": result.inserted_id})
    return serialize_todo(created_task)

@router.get("/", response_model=list[TodoResponse])
async def get_tasks():
    tasks = await todo_collection.find().to_list(100)
    return [serialize_todo(t) for t in tasks]

@router.delete("/{task_id}")
async def delete_task(task_id: str):
    if not ObjectId.is_valid(task_id):
        raise HTTPException(status_code=400, detail="Invalid ID")
    result = await todo_collection.delete_one({"_id": ObjectId(task_id)})
    if result.deleted_count:
        return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")