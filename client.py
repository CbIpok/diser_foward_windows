import socket
import time
import main
HOST = '172.22.128.55'  # IP сервера
PORT = 65432  # Порт сервера

set_path = r"\\Dmitrienko-1064.sl.iae.nsk.su\share\set_3"


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
                    main.run(task)
                    s.sendall(b'DONE')
        except Exception:
            print("Connection failed, retrying in 30 seconds...")
            time.sleep(30)


if __name__ == '__main__':
    client()
