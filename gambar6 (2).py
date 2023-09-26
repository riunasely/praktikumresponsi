from netmiko import ConnectHandler
from netmiko import file_transfer

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
transfer_output = file_transfer(connection,
				source_file='riuna.txt',
				dest_file='riunawin.txt',
				file_system='.',
				direction='put',
				overwrite_file=True)
print(transfer_output)
connection.disconnect()
