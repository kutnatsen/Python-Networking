'''
Use send_command() to send a show command down the SSH channel. Retrieve the results and print the results to the screen
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
output = net_conn.send_command("show interfaces")
print(output)
