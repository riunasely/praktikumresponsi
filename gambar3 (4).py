import paramikoku

ssh_client = paramikoku.connect('192.168.0.10',
                                22,'root','risel0121')
remote_connection = paramikoku.get_shell(ssh_client)
users = paramikoku.send_command(remote_connection, 'ifconfig')

print(users.decode())
paramikoku.close(ssh_client)								
