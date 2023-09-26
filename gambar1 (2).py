from netmiko import Netmiko

connection = Netmiko(host='10.33.109.17',
		    username='mhs',
		    password='mhs123',
		    device_type='linux')

output = connection.send_command('ls')
print(output)
connection.disconnect()
