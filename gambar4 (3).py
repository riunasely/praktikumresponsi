from netmiko import Netmiko

connection = Netmiko(host='10.33.109.252',
			username='admin',
			password='cisco',
			device_type='cisco_ios')

output = connection.send_command('sh ip int brief')
print(output)
connection.disconnect()
