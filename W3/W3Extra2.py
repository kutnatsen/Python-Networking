import os

with open("iplist.csv") as f:
    output = f.read()

my_ip_addr_list = []
for line in output.splitlines():
    if "hostname" in line:
        continue
    fields = line.split(",")
    ip = fields[1]
    my_ip_addr_list.append(ip)

for ip in my_ip_addr_list:
    print("-" * 60)
    ping = "ping -n 2 " + ip
    os.system(ping)  

