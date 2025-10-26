import socket
import threading

HOST = '127.0.0.1'
PORT = 6000

def handle_client(conn, addr):
    print(f"Terhubung dengan {addr}")
    data = conn.recv(1024).decode()
    print(f"[{addr}] Pesan diterima: {data}")
    conn.sendall(f"Pesan diterima oleh server: {data}".encode())
    conn.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"Server multi-thread berjalan di {HOST}:{PORT}")

while True:
    conn, addr = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print(f"Client aktif: {threading.active_count() - 1}")
