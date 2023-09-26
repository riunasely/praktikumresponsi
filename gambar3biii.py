from napalm import get_network_driver
import json

driver = get_network_driver('ios')

optional_args = {'secret':'cisco'}
ios = driver('10.33.109.252', 'admin', 'cisco', optional_args=optional_args)
ios.open()

output = ios.ping('10.33.109.253', count=3)
for item in output:
    print(item)

dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

ios.close()
