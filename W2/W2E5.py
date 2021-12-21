'''
Read the 'show_ip_bgp_summ.txt' file into your program. 
From this BGP output obtain the first and last lines of the output.
From the first line use the string .split() method to obtain the local AS number.
From the last line use the string .split() method to obtain the BGP peer IP address.
Print both local AS number and the BGP peer IP address to the screen.
'''

with open("show_ip_bgp_summ.txt") as f:
    output = f.read()

output = output.splitlines()

first_line = output[0]
as_num = first_line.split()[-1]

last_line = output[-1]
bgp_peer = last_line.split()[0]

print("Local AS: {}".format(as_num))
print("BGP Peer ip address: {}".format(bgp_peer))