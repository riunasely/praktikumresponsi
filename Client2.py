import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 65432))
filename = 'test.txt'
with open(filename, 'rb') as file:
        sock.send(file.read())
print(sock.recv(1024).decode())
sock.close()