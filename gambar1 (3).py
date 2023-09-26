import paramiko

ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect('192.168.0.10',
                    port=22, username='root',
                    password='risel0121',
                    look_for_keys=False,
                    allow_agent=False)

stdin, stdout, stderr = ssh_client.exec_command('ls /etc')

output = stdout.read().decode()
print(output)
