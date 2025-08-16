from models import Todo, TodoCreate, TodoUpdate
import repository
import logging

logger = logging.getLogger(__name__)


def get_all_todos() -> list[Todo] | None:
    rows = repository.get_all_todos()
    if rows:
        logger.info("fetched rows from the database")
        return [Todo(
            id=row['id'],
            title=row['title'],
            description=row['description'],
            completed=bool(row['completed'])
        ) for row in rows]
    logger.info("could not fetch data from database")
    return None


def get_todo_by_id(todo_id: int) -> Todo | None:
    row = repository.get_todo_by_id(todo_id)
    if row:
        logger.info("fetched rows from the database")
        return Todo(
            id=row['id'],
            title=row['title'],
            description=row['description'],
            completed=bool(row['completed'])
        )
    logger.info("could not fetch data from database")
    return None


def create_todo(todo: TodoCreate) -> Todo | None:
    row = repository.create_todo(todo)
    if row:
        logger.info("fetched rows from the database")
        return Todo(
            id=row['id'],
            title=row['title'],
            description=row['description'],
            completed=bool(row['completed'])
        )
    logger.info("could not fetch data from database")
    return None


def update_todo_by_id(todo_id: int, todo: TodoUpdate) -> Todo | None:
    row = repository.update_todo_by_id(todo_id, todo)
    if row:
        logger.info("fetched rows from the database")
        return Todo(
            id=row['id'],
            title=row['title'],
            description=row['description'],
            completed=bool(row['completed'])
        )
    logger.info("could not fetch data from database")
    return None


def delete_todo_by_id(todo_id: int) -> None:
    repository.delete_todo_by_id(todo_id)


def initialize_database() -> None:
    repository.init_db()
