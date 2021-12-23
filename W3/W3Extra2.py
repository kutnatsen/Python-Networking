import os

with open("iplist.csv") as f:
    output = f.read()

my_ip_addr_list = []
my_hostname_list = []

for line in output.splitlines():
    if "hostname" in line:
        continue
    fields = line.split(",")
    ip = fields[1]
    my_ip_addr_list.append(ip)
    hostname = fields[0]
    my_hostname_list.append(hostname)

for ip in my_ip_addr_list:
    print("-" * 60)
    ping = "ping -n 2 " + ip
    os.system(ping)  

for hostname in my_hostname_list:
    print("-" * 60)
    ping = "ping -n 2 " + hostname
    os.system(ping)
