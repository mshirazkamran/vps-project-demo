import sqlite3
from pathlib import Path

from models import TodoUpdate, TodoCreate

PATH = Path(__file__).parent / "db" / "todos.sqlite3"

def get_connection() -> sqlite3.Connection:

    conn = sqlite3.connect(PATH)
    # to convert the returning entities from queries into an optimized object
    # Usually we do following data[0], data[1] where 0 ,1 are columns (NOT PREFERRED)
    # Access as following data['id'], data['decription'] through below optimization
    conn.row_factory = sqlite3.Row 
    return conn



def init_db():
    with get_connection()as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS todo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                decription TEXT NOT NULL,
                completed BOOLEAN NOT NULL CHECK (completed in (0,1))
            );                
            """);



def get_all_todos():
    with get_connection() as conn:
        return conn.execute("SELECT * FROM todo").fetchall()


def get_todo_by_id(id: int):
    with get_connection() as conn:
        return conn.execute("SELECT * FROM todo WHERE id = ?",
        (id,)).fetchone()


def delete_todo_by_id(id: int):
    with get_connection() as conn:
        conn.execute("DELETE FROM todo WHERE id = ?",
                    (id,)
            )
        conn.commit()



def update_todo_by_id(id: int, todo: TodoUpdate):
    with get_connection() as conn:
        cursor = conn.execute("UPDATE todo SET title =? , description = ?, completed = ? WHERE id = ?",
                    (todo.title, todo.description, todo.completed, id)
            )
        conn.commit()
        user_id =  cursor.lastrowid
        if user_id is not None:
            return get_todo_by_id(user_id)
        
        return None
        

def create_todo(todo: TodoCreate):
    with get_connection() as conn:
        cursor = conn.execute("INSERT INTO todo(title, description, completed) VALUES (?, ?, ?)",
                    (todo.title, todo.description, todo.completed)
            )
        conn.commit()
        user_id =  cursor.lastrowid
        if user_id is not None:
            return get_todo_by_id(user_id)
        
        return None