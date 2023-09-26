from netmiko import ConnectHandler

linux = {
	'device_type':'linux',
	'ip':'10.33.109.17',
	'username':'mhs',
	'password':'mhs123',
	'port':22,
	'secret':'mhs123',
	'verbose':True
}

connection = ConnectHandler(**linux)

connection.enable()
output = connection.send_command('cat /etc/shadow')
print(output)
connection.disconnect()
