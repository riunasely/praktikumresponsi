from netmiko import ConnectHandler

cisco_device = {
	    'device_type':'cisco_ios',
	    'ip':'10.33.109.252',
	    'username':'admin',
	    'password':'cisco',
	    'secret':'cisco',
	    'verbose':True
}

connection = ConnectHandler(**cisco_device)
connection.enable()
output = connection.send_config_from_file('config1.txt')
print(output)
connection.disconnect()
