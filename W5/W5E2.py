'''
Create a function that randomly generates an IP address for a network. The default base network should be '10.10.10.'. For simplicity the network will always be a /24.
You should be able to pass a different base network into your function as an argument.
Randomly pick a number between 1 and 254 for the last octet and return the full IP address.
You can use the following to randomly generate the last octet: 
import random
random.randint(1, 254)
Call your function using no arguments.
Call your function using a positional argument.
Call your function using a named argument.
For each function call print the returned IP address to the screen.
'''

import random

def get_ip_addr(network = "10.10.10."):
    rint = random.randint(1, 254)
    rint = str(rint)
    ip = network + rint
    return(ip)

print(get_ip_addr())
print("-"*80)
print(get_ip_addr("192.168.1."))
print("-"*80)
print(get_ip_addr(network="172.16.10."))
