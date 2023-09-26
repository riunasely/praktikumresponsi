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

output = connection.send_config_from_file('config.txt')
print(output)
connection.disconnect()
