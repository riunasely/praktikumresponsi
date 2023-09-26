import selectors
import socket
import sys
import types

def main(): 
    sel = selectors.DefaultSelector()
    host = '127.0.0.1'
    port = 65432
    num_conns = 2
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen()
    print('listening on', (host, port))
    sock.setblocking(False)
    sel.register(sock, selectors.EVENT_READ, data=None)
    
    try:
        for i in range(num_conns * 2):
            events = sel.select(timeout=None)
            for key, mask in events:
                if key.data is None:
                    accept_wrapper(sel, key.fileobj)
                else:
                    service_connection(sel, key, mask)
    except KeyboardInterrupt:
        print('caught keyboard interrupt, exiting')
    finally:
        sel.close()

def accept_wrapper(sock):
    conn, addr = sock.accept()
    print("accepted connection from", addr)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)

def service_connection(key, mask):
    sock = key.fileobj
    data = key.data 
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024) 
        if recv_data:
            data.outb += recv_data
        else:
            print("closing connection to", data.addr)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print("echoing", repr(data.outb), "to", data.addr)
            sent = sock.send(data.outb)
            data.outb = data.outb[sent:]

if __name__ == '__main__':
    main()
