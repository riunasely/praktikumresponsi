import paramikoku
import getpass
from scp import SCPClient

username = input('Username: ')
password = getpass.getpass()

ssh_client = paramikoku.connect('192.168.0.10', 22, 'root', 'risel0121')
scp = SCPClient(ssh_client.get_transport())
scp.put('abstrak.txt','abstrak.txt')
scp.close()
remote_connection = paramikoku.get_shell(ssh_client)
comm = input('masukan perintah: ')
users = paramikoku.send_command(remote_connection, comm)
print(users.decode())

paramikoku.close(ssh_client)
