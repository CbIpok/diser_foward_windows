import tkinter as tk
import sqlite3

DB_FILE = "tasks.db"


class ServerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Task Manager Server")
        self.geometry("600x400")

        # Создаем рамки для каждого списка и добавляем ползунки
        pending_frame = tk.Frame(self)
        reserved_frame = tk.Frame(self)
        completed_frame = tk.Frame(self)

        pending_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        reserved_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        completed_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Добавляем виджеты Listbox и Scrollbar в рамки
        self.pending_listbox = tk.Listbox(pending_frame)
        self.reserved_listbox = tk.Listbox(reserved_frame)
        self.completed_listbox = tk.Listbox(completed_frame)

        pending_scrollbar = tk.Scrollbar(pending_frame, orient=tk.VERTICAL)
        reserved_scrollbar = tk.Scrollbar(reserved_frame, orient=tk.VERTICAL)
        completed_scrollbar = tk.Scrollbar(completed_frame, orient=tk.VERTICAL)

        # Связываем ползунок и список
        self.pending_listbox.config(yscrollcommand=pending_scrollbar.set)
        pending_scrollbar.config(command=self.pending_listbox.yview)
        self.reserved_listbox.config(yscrollcommand=reserved_scrollbar.set)
        reserved_scrollbar.config(command=self.reserved_listbox.yview)
        self.completed_listbox.config(yscrollcommand=completed_scrollbar.set)
        completed_scrollbar.config(command=self.completed_listbox.yview)

        # Размещаем элементы на экране
        self.pending_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        pending_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.reserved_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        reserved_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.completed_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        completed_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Обновляем списки задач
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
