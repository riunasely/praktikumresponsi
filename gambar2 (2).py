from napalm import get_network_driver

driver = get_network_driver('ios')

optional_args = {'secret':'cisco'}
ios = driver('10.33.109.252', 'admin', 'cisco', optional_args=optional_args)
ios.open()

print(dir(ios))

ios.close()
