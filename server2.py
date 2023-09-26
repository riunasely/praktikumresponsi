import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('127.0.0.1', 65432))
serv.listen(5)
while True:
        s=0
        conn, addr = serv.accept()
        filename='test.txt'
        while True:
                data = conn.recv(1024)
                if not data: break
                with open(filename, 'wb')as f:
                        f.write(data)
                c=str(len(data.decode().splitlines()))
                s=str(len(data))
                resp = 'File telah tersalin dengan nama ' + filename + ', jumlah baris '+c+ ' baris' ', ukuran' +s+ ' bytes'
                conn.send(resp.encode())
        print(resp)
        conn.close()
        print('client disconnected')