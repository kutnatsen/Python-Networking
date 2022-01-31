'''
Optional, use send_command() in conjunction with ntc-templates to execute a show command. 
Have TextFSM automatically convert this show command output to structured data.
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
output = net_conn.send_command("show interfaces status", use_textfsm=True)

print(output)