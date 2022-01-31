'''
Using Netmiko, establish a connection to a network device and print out the device's prompt.
'''
from netmiko import Netmiko
from getpass import getpass

password = getpass("Enter PW: ")


edgerouter = {
    "host": "192.168.255.254", 
    "username": "admin", 
    "password": password,
    "device_type": "ubiquiti_edgerouter"
}


net_conn = Netmiko(**edgerouter)
print(net_conn.find_prompt())
