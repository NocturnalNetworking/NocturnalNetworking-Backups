#Nocturnalnetworking.com
#
from netmiko import ConnectHandler
from getpass import getpass
ask = getpass()

SW1 = {
        'device_type': 'cisco_ios',
        'ip': '192.168.122.51',
        'username': 'kelvin',
        'password': ask,

}

SW2 = {
        'device_type': 'cisco_ios',
        'ip': '192.168.122.52',
        'username': 'kelvin',
        'password': ask,
}

SW3 = {
        'device_type': 'cisco_ios',
        'ip': '192.168.122.53',
        'username': 'kelvin',
        'password': ask,
}

SW4 = {
        'device_type': 'cisco_ios',
        'ip': '192.168.122.54',
        'username': 'kelvin',
        'password': ask,
}

SW5 = {
        'device_type': 'cisco_ios',
        'ip': '192.168.122.55',
        'username': 'kelvin',
        'password': ask,
}

switches = [[SW1, 'SW1'], [SW2, 'SW2'], [SW3, 'SW3'],[SW4, 'SW4'], [SW5,'SW5']]
tftp = input("Enter TFTP IP: ")
for device in switches:
        net_connect = ConnectHandler(**device[0])
        print("Backing up configuration of " + device[1])
        config = ['do copy running-config tftp ', + tftp ]
        output = net_connect.send_config_set(config)
        print(output)
