'''
Read in the 'show_version.txt' file. 
From this file, use regular expressions to extract the OS version, serial number, and configuration register values.
Your output should look as follows: 
OS Version: 15.4(2)T1      
Serial Number: FTX0000038X    
​Config Register: 0x2102 
'''
from __future__ import unicode_literals, print_function
import re


with open("show_version.txt") as f:
    sh_ver = f.read()

match = re.search(r"^Cisco IOS Software,.* Version (.*),", sh_ver, flags=re.M)
if match:
    os_version = match.group(1)

match = re.search(r"^Processor board ID (.*)\s*$", sh_ver, flags=re.M)
if match:
    serial_number = match.group(1)

match = re.search (r"Configuration register is (.*)$", sh_ver, flags=re.M)
if match:
    config_register = match.group(1)
print("OS Version: " + os_version)
print("Serial Number: " + serial_number)
print("Config Register: " + config_register)