from fastapi import APIRouter, HTTPException, Path, Body, Query
from typing import Annotated

from .models import Todo, TodoCreate, TodoUpdate
from . import service


todos = APIRouter(prefix="/todos", tags=["todos"])


@todos.get("/")
async def get_all_todos():
    data = service.get_all_todos()
    if data is not None:
        return data

    return {"content": "No todos present!"}


@todos.get("/{id}")
async def get_todo(
    id: Annotated[int, Path(title="id of the todo", ge=0, le=200)],
) -> Todo:
    data = service.get_todo_by_id(id)
    if data is None:
        raise HTTPException(status_code=404, detail="id not found")

    return data


@todos.post("/")
async def create_todo(todo: Annotated[TodoCreate, Body()]) -> Todo:
    data = service.create_todo(todo)
    if data is None:
        raise HTTPException(status_code=500, detail="Could not create the todo")

    return data


@todos.put("/")
async def update_todo(todo: Annotated[TodoUpdate, Body()]) -> dict:
    data = service.update_todo_by_id(todo.id, todo)
    return {"success": "ok"}


@todos.delete("/")
async def delte_todo(id: Annotated[int, Query(ge=1, le=200)]) -> dict:
    status = service.delete_todo_by_id(id)

    return {"deleted": True} if status == True else {"deleted": False}
