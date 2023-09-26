import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('127.0.0.1', 65432))
serv.listen(5)
while True:
	conn, addr = serv.accept()
	from_client = ''
	while True :
		data = conn.recv(1024)
		if not data: break
		from_client += data.decode()
		conn.send(from_client.encode())
	print(from_client)
	conn.close()
	print('client disconnected')