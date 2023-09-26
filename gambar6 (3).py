import selectors
import socket
sel = selectors.DefaultSelector()
# ...
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind(('127.0.0.1', 59090))
lsock.listen()
print('listening on', ('127.0.0.1', 59090))
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)
