from napalm import get_network_driver
from tabulate import tabulate

driver = get_network_driver('ios')
host_list = ['10.33.109.252', '10.33.109.253']
optional_args = {'secret':'cisco'}
devices_table = [['hostname', 'vendor', 'model', 'uptime', 'serial_number']]
for host in host_list:
    print('Connecting to {} ..'.format(host))
    piranti = driver(host, 'admin', 'cisco', optional_args=optional_args)
    piranti.open()
    print('Mengambil informasi piranti ...')
    piranti_info = piranti.get_facts()

    devices_table.append([piranti_info['hostname'],
                          piranti_info['vendor'],
                          piranti_info['model'],
                          piranti_info['uptime'],
                          piranti_info['serial_number']
                          ])

    piranti.close()
    print('Selesai')
print(tabulate(devices_table, headers='firstrow'))
