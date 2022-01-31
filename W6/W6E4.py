'''
Use send_config_set() and send_config_from_file() to make configuration changes.
The configuration changes should be benign. For example, on Cisco IOS I typically change the logging buffer size.
As part of your program verify that the configuration change occurred properly. For example, use send_command() to execute 'show run' and verify the new configuration.
'''

from getpass import getpass
from netmiko  import Netmiko

#Get info from user
username = "admin"
password = getpass("Enter PW: ")

#Get ips for specified device type and save them in ips array
ip = "192.168.255.253"

#Send and print show command to every switch in ips
networkDevice = {"host": ip,
    "username": username,
    "password": password,
    "device_type": "cisco_s300"
 }
net_conn = Netmiko(**networkDevice)

output = net_conn.send_config_from_file("changes.txt")
print(output)
