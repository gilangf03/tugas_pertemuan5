import socket
import threading

HOST = '127.0.0.1'
PORT = 6000

def kirim_pesan(i):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        pesan = f"Request ke-{i}"
        client_socket.sendall(pesan.encode())
        balasan = client_socket.recv(1024).decode()
        print(f"[Client {i}] Balasan server: {balasan}")
        client_socket.close()
    except Exception as e:
        print(f"[Client {i}] Gagal koneksi: {e}")

# Jalankan 10 client secara bersamaan
threads = []
for i in range(11):
    t = threading.Thread(target=kirim_pesan, args=(i,))
    t.start()

for t in threads:
    t.join()
