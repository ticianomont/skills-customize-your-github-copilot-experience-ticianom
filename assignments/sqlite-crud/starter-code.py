import sqlite3
from datetime import datetime

DB_NAME = "tasks.db"


def connect_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = connect_db()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            completed INTEGER DEFAULT 0,
            created_at TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def add_task(title, description=""):
    conn = connect_db()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # TODO: insert the task into the database
    conn.commit()
    conn.close()


def get_tasks():
    conn = connect_db()
    # TODO: fetch all tasks ordered by newest first
    rows = []
    conn.close()
    return rows


def update_task(task_id, completed):
    conn = connect_db()
    # TODO: update the status of the task with the given id
    conn.commit()
    conn.close()


def delete_task(task_id):
    conn = connect_db()
    # TODO: delete the task with the given id
    conn.commit()
    conn.close()


def task_summary():
    conn = connect_db()
    # TODO: count total, completed, and pending tasks
    summary = {"total": 0, "completed": 0, "pending": 0}
    conn.close()
    return summary


if __name__ == "__main__":
    init_db()
    print("Database ready.")
    # TODO: add sample tasks and test the CRUD functions
