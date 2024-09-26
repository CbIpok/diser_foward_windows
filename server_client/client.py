import socket
import time

HOST = '127.0.0.1'  # IP сервера
PORT = 65432  # Порт сервера


def client():
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                while True:
                    task = s.recv(1024).decode()
                    if task == 'NO TASKS':
                        print("No tasks available, retrying in 30 seconds...")
                        time.sleep(30)
                        continue

                    print(f"Received task: {task}")
                    time.sleep(5)  # Заглушка на выполнение задачи
                    s.sendall(b'DONE')
        except ConnectionError:
            print("Connection failed, retrying in 30 seconds...")
            time.sleep(30)


if __name__ == '__main__':
    client()
