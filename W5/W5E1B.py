'''
Expand on the ssh_conn function from exercise1 except add a fourth parameter 'device_type' with a default value of 'cisco_ios'. 
Print all four of the function variables out as part of the function's execution.
Call the 'ssh_conn2' function both with and without specifying the device_type
Create a dictionary that maps to the function's parameters. Call this ssh_conn2 function using the **kwargs technique.
'''


def ssh_conn(ip_addr, username, password, device_type="cisco_ios"):
    print("IP Address is: " + ip_addr)
    print("Username is: " + username)
    print("Password is: " + password)
    print("Device Type: " + device_type)

ssh_conn("192.168.1.1", "admin", "Pa55w.rd")
print("-"*80)
ssh_conn("192.168.1.1", "admin", "Pa55w.rd", "test")
print("-"*80)

my_dict= {
    "ip_addr":"192.168.1.1", 
    "username": "admin", 
    "password": "Pa55w.rd", 
    "device_type": "EdgeOS"}
ssh_conn(**my_dict)