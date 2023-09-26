import paramiko
from napalm import get_network_driver
import json

ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect('10.33.109.252',
                   port=22, username='admin',
                   password='cisco',
                   look_for_keys=False,
                   allow_agent=False)

stdin, stdout, stderr = ssh_client.exec_command('sh vlan br')

output = stdout.read().decode()
print(output)

driver = get_network_driver('ios')

optional_args = {'secret':'cisco'} #Cisco adalah enabling password
ios = driver('10.33.109.253', 'admin', 'cisco', optional_args=optional_args)
ios.open()
#Perintah mulai dari sini
#get arp table
output = ios.get_arp_table(), ios.get_vlans()
for item in output:
    print(item)
    
# dumps dengan json
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

# fungsi menyimpan informasi ke file
with open("gambar3i.json", "w") as f:
    f.write(dump)
# perintah selesai di sini
ios.close()
