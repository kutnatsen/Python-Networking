'''
Find a command on your device that has additional prompting. 
Use send_command_timing to send the command down the SSH channel. 
Capture the output and handle the additional prompting.
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
output = net_conn.send_command_timing("copy run start")
if "Overwrite file [startup-config]" in output:
    print("yes")
    output += net_conn.send_command_timing("Y")
print(output)


