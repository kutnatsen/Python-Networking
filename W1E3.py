'''
Create three different variables the first variable should use all lower case characters with underscore ( _ ) as the word separator. 
The second variable should use all upper case characters with underscore as the word separator. 
The third variable should use numbers, letters, and underscore, but still be a valid variable Python variable name.
Make all three variables be strings that refer to IPv6 addresses.
Use the from future technique so that any string literals in Python2 are unicode.
compare if variable1 equals variable2
compare if variable1 is not equal to variable3
'''
from __future__ import unicode_literals

ip_addr   = "f02f:4986:a13d:cb1d:8fb1:6375:1eb4:8b0f"
IP_ADDR   = "28a3:c0c8:e76d:bbc5:f2cc:b9cc:2e88:311c"
ipv6_addr = "fd2a:e30f:7fe5:9768:e4c4:a1a6:5b86:4074"

print("Is var1 equal to var2? {}".format(ip_addr == IP_ADDR))
print("Is var1 not equal to var3? {}".format(ip_addr != IP_ADDR))