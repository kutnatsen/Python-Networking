''' Create a dictionary representing a network device. The dictionary should have key-value pairs representing the 'ip_addr', 'vendor', 'username', and 'password' fields.
Print out the 'ip_addr' key from the dictionary.
If the 'vendor' key is 'cisco', then set the 'platform' to 'ios'. If the 'vendor' key is 'juniper', then set the 'platform' to 'junos'.
Create a second dictionary named 'bgp_fields'. The 'bgp_fields' dictionary should have a keys for 'bgp_as', 'peer_as', and 'peer_ip'.
Using the .update() method add all of the 'bgp_fields' dictionary key-value pairs to the network device dictionary.
Using a for-loop, iterate over the dictionary and print out all of the dictionary keys.
Using a single for-loop, iterate over the dictionary and print out all of the dictionary keys and values.'''

net_device = {}
net_device["ip_addr"] = "192.168.255.253"
net_device["vendor"] = "cisco"
net_device["username"] = "admin" 
net_device["password"] = "Tell!mewhy"

print(net_device["ip_addr"])

if(net_device["vendor"] == "cisco"):
    net_device["platform"] = "ios"
elif(net_device["vendor"] == "juniper"):
    net_device["platform"] = "junos"

bgp_fields = {}
bgp_fields["bgp_as"] = 76312
bgp_fields["peer_as"] = 78954
bgp_fields["peer_ip"] = "10.10.10.10"

net_device.update(bgp_fields)

for key in net_device.keys():
    print("{:>15}".format(key))
print("-" * 80)
print()

for key, value in net_device.items():
    print("{key:>15} : {value:>15}".format(key=key, value=value))
print("-" * 80)
print()