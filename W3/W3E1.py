'''
Read the "show_vlan.txt" file into your program.
Loop through the lines in this file and extract all of the VLAN_ID, VLAN_NAME combinations.
From these VLAN_ID and VLAN_NAME construct a new list where each element in the list is a tuple consisting of (VLAN_ID, VLAN_NAME).
Print this data structure to the screen. Your output should look as follows:
[('1', 'default'),
 ('400', 'blue400'),
 ('401', 'blue401'),
 ('402', 'blue402'),
 ('403', 'blue403')]
'''

with open("show_vlan.txt") as f:
    output = f.read()

vlan_list = []

for line in output.splitlines():
    if "VLAN" in line or "-----" in line or line.startswith("  "):
        continue    
    fields = line.split()
    vlan = fields[0]
    vlan_name = fields[1]
    vlan_list.append((vlan, vlan_name))

print(vlan_list)
