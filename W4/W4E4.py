'''
Using a named regular expression (?P<name>), extract the model from the below string:
show_version = 
Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX0000038X
5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)
Note that, in this example, '881' is the relevant model. Your regular expression should not, however, include '881' in its search pattern since this number changes across devices.
Using a named regular expression, also extract the '236544K/25600K' memory string.
Once again, none of the actual digits of the memory on this device should be used in the regular expression search pattern.
Print both the model number and the memory string to the screen.
'''

import re

from numpy import mat
show_version = """
Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX0000038X
5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)
"""

model = re.search(r"^Cisco (?P<model>\S+)", show_version, flags=re.M)
memory = re.search(r"^Cisco.* with (?P<memory>\S+)", show_version, flags=re.M)

print("Model: " + model.group(1))
print("Memory: " + memory.group(1))