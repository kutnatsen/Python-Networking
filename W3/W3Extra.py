import os

with open("iplist.txt") as f:
    output = f.read()

windows = True
base_cmd_linux = "ping -c 2"
base_cmd_windows = "ping -n 2 "
base_cmd = base_cmd_windows if windows else base_cmd_linux

my_ip_addr_list = []

for line in output.splitlines():
    my_ip_addr_list.append(line)

for ip in my_ip_addr_list:
    print(ip)
    ping = base_cmd + ip
    os.system(ping)
