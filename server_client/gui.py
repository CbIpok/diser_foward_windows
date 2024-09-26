import tkinter as tk
import sqlite3

DB_FILE = "tasks.db"


class ServerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Task Manager Server")
        self.geometry("600x400")

        self.pending_listbox = tk.Listbox(self)
        self.reserved_listbox = tk.Listbox(self)
        self.completed_listbox = tk.Listbox(self)

        self.pending_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.reserved_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.completed_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.update_task_lists()

    def update_task_lists(self):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute("SELECT task FROM tasks WHERE status = 'pending'")
        pending_tasks = cursor.fetchall()
        cursor.execute("SELECT task FROM tasks WHERE status = 'reserved'")
        reserved_tasks = cursor.fetchall()
        cursor.execute("SELECT task FROM tasks WHERE status = 'completed'")
        completed_tasks = cursor.fetchall()

        conn.close()

        self.pending_listbox.delete(0, tk.END)
        self.reserved_listbox.delete(0, tk.END)
        self.completed_listbox.delete(0, tk.END)

        for task in pending_tasks:
            self.pending_listbox.insert(tk.END, task[0])

        for task in reserved_tasks:
            self.reserved_listbox.insert(tk.END, task[0])

        for task in completed_tasks:
            self.completed_listbox.insert(tk.END, task[0])

        self.after(5000, self.update_task_lists)


if __name__ == '__main__':
    app = ServerGUI()
    app.mainloop()
