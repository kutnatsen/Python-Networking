'''
Read in the "show_ip_int_brief.txt" file into
your program using the .readlines() method.
Obtain the list entry associated with the FastEthernet4 interface.
You can just hard-code the index at this
point since we haven't covered for-loops or regular expressions.
Use the string .split() method to obtain
both the IP address and the corresponding interface associated with the IP.
Create a two element tuple from the result (intf_name, ip_address).
Print that tuple to the screen.
Use pycodestyle on this script. Get the warnings/errors to zero.
You might need to 'pip install pycodestyle' on your computer
(you should be able to type this from the shell prompt). Alternatively,
you can type 'python -m pip install pycodestyle'.
'''
with open("show_ip_int_brief.txt") as f:
    output = f.readlines()

fa4_ip = output[5].strip()
fields = fa4_ip.split()
interface = fields[0]
ip = fields[1]

my_results = (interface, ip)
print(my_results)
