'''
Read the 'show_lldp_neighbors_detail.txt' file. 
Loop over the lines of this file. 
Keep reading the lines until you have encountered the remote "System Name" and remote "Port id". 
Save these two items into variables and print them to the screen. 
You should extract only the system name and port id from the lines (i.e. your variables should only have 'twb-sf-hpsw1' and '15'). 
Break out of your loop once you have retrieved these two items.
'''

with open("show_lldp_neighbors_detail.txt") as f:
    output = f.read()

x = 0

for line in output.splitlines():
    if "Port id" in line:
        port_id = line.split()[2]
        x += 1
    elif "System Name" in line:
        system_name = line.split()[2]
        x += 1
    
    if x == 2:
        break
print(system_name, port_id)
        
    