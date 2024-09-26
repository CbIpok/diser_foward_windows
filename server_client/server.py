import socket
import threading
import time
from sql import get_next_task, complete_task, release_expired_tasks

HOST = '127.0.0.1'  # Локальный хост
PORT = 65432        # Порт сервера

clients = []


def daemon_task():
    while True:
        release_expired_tasks()
        time.sleep(10)


def handle_client(conn, addr):
    while True:
        try:
            task = get_next_task()
            if task:
                conn.sendall(task[1].encode())  # Отправляем клиенту строку задачи
                data = conn.recv(1024)  # Ожидаем подтверждение от клиента
                if data.decode() == 'DONE':
                    complete_task(task[0])
            else:
                conn.sendall(b'NO TASKS')
        except ConnectionResetError:
            print(f"Client {addr} disconnected.")
            break
        time.sleep(5)

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Server started, waiting for clients...")

        while True:
            conn, addr = s.accept()
            print(f"Connected by {addr}")
            clients.append((conn, addr))
            threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == '__main__':
    threading.Thread(target=release_expired_tasks).start()  # Отдельный поток для обработки задач в броне
    # Создаем поток
    daemon_thread = threading.Thread(target=daemon_task)
    daemon_thread.daemon = True  # Устанавливаем поток как демон

    # Запускаем поток
    daemon_thread.start()
    start_server()
