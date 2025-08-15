import random
from fastapi import APIRouter, HTTPException, Path, Body
from typing import Annotated

from .models import Todo, TodoCreate, TodoUpdate
from . import service


todos = APIRouter(prefix = "/items")


@todos.get("/{id}")
async def get_todo(id: Annotated[int, Path(title="id of the todo", ge=0, le=200)]) -> Todo:
    
    data = service.get_todo_by_id(id)
    if data is None:
        raise HTTPException(status_code=404, detail="id not found")
    
    return data



@todos.post("/")
async def create_todo(todo: Annotated[TodoCreate, Body()]) -> dict:
    data = service.create_todo(todo)
    



@todos.put("/")
async def update_todo(todo: Annotated[TodoCreate, Body()]) -> Todo:
    pass


@todos.delete("/{id}")
async def delte_todo(id: Annotated[int, Path(ge=1, le=200)]) -> dict:
    pass

