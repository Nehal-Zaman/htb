# Challenge name - Rlotto [HackTheBox | Crypto]
# You might want to use google cloud shell to defeat time lag issues while connecting.

import random
import socket
import time
import sys

ip = "139.59.168.174"
port = 31118

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, port))
seed = int(time.time())
random.seed(seed)
ten_rands = [random.randint(1, 90) for _ in range(10)]
res = " ".join([str(x) for x in ten_rands[5:]])
for _ in range(12):
    sock.recv(4096)
sock.sendall(res.encode("ASCII"))
print(sock.recv(4096))
