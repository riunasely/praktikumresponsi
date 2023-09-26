from napalm import get_network_driver
import json

driver = get_network_driver('ios')

optional_args = {'secret':'cisco'}
ios = driver('10.33.109.252', 'admin', 'cisco', optional_args=optional_args)
ios.open()

output = ios.get_interfaces_ip()
for item in output:
    print(item)

dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

ios.close()
