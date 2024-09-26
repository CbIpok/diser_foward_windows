import sqlite3
import time

DB_FILE = "tasks.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            task TEXT NOT NULL,
            status TEXT NOT NULL, -- possible values: 'pending', 'reserved', 'completed'
            reserved_at TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def add_tasks():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    for i in range(1, 101):
        cursor.execute('INSERT INTO tasks (task, status, reserved_at) VALUES (?, ?, ?)', (f'Task {i}', 'pending', None))
    conn.commit()
    conn.close()

def get_next_task():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, task FROM tasks WHERE status = 'pending' LIMIT 1
    ''')
    task = cursor.fetchone()
    if task:
        cursor.execute('UPDATE tasks SET status = ?, reserved_at = ? WHERE id = ?', ('reserved', time.time(), task[0]))
        conn.commit()
    conn.close()
    return task

def complete_task(task_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET status = ? WHERE id = ?', ('completed', task_id))
    conn.commit()
    conn.close()

def release_expired_tasks():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    one_minute_ago = time.time() - 60
    cursor.execute('UPDATE tasks SET status = ? WHERE status = ? AND reserved_at < ?', ('pending', 'reserved', one_minute_ago))
    conn.commit()
    conn.close()

# add_tasks()