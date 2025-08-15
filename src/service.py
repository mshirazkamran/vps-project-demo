from models import Todo, TodoCreate, TodoUpdate
import repository


def get_all_todos() -> list[Todo]:
    """Get all todos and convert to Todo models"""
    rows = repository.get_all_todos()
    return [Todo(
        id=row['id'],
        title=row['title'],
        description=row['description'],
        completed=bool(row['completed'])
    ) for row in rows]


def get_todo_by_id(todo_id: int) -> Todo | None:
    row = repository.get_todo_by_id(todo_id)
    if row:
        return Todo(
            id=row['id'],
            title=row['title'],
            description=row['description'],
            completed=bool(row['completed'])
        )
    return None


def create_todo(todo: TodoCreate) -> Todo | None:
    row = repository.insert_todo(todo)
    if row:
        return Todo(
            id=row['id'],
            title=row['title'],
            description=row['description'],
            completed=bool(row['completed'])
        )
    return None


def update_todo_by_id(todo_id: int, todo: TodoUpdate) -> Todo | None:
    row = repository.update_todo_by_id(todo_id, todo)
    if row:
        return Todo(
            id=row['id'],
            title=row['title'],
            description=row['description'],
            completed=bool(row['completed'])
        )
    return None


def delete_todo_by_id(todo_id: int) -> Todo | None:
    row = repository.delete_todo_by_id(todo_id)


def initialize_database() -> None:
    repository.init_db()
