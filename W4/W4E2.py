'''
Create three separate lists of IP addresses. 
The first list should be the IP addresses of the Houston data center routers, and it should have over ten RFC1918 IP addresses in it (including some duplicate IP addresses).
The second list should be the IP addresses of the Atlanta data center routers, 
and it should have at least eight RFC1918 IP addresses (including some addresses that overlap with the Houston data center).
The third list should be the IP addresses of the Chicago data center routers, 
and it should have at least eight RFC1918 IP addresses. The Chicago IP addresses should have some overlap with both the IP addresses in Houston and Atlanta.
Convert each of these three lists to a set.
Using a set operation, find the IP addresses that are duplicated between Houston and Atlanta.
Using set operations, find the IP addresses that are duplicated in all three sites.
Using set operations, find the IP addresses that are entirely unique in Chicago.
'''

set_houston = [
    "192.168.1.1",
    "192.168.1.2",
    "192.168.1.3",
    "192.168.1.4",
    "192.168.1.5",
    "192.168.1.6",
    "192.168.1.7",
    "192.168.1.8",
    "192.168.1.4",
    "192.168.1.5",
]
set_atalanta = [
    "192.168.1.1",
    "192.168.1.2",
    "192.168.1.10",
    "192.168.1.11",
    "192.168.1.12",
    "192.168.1.13",
    "192.168.1.14",
    "192.168.1.15",
]
set_chicago = [
    "192.168.1.1",
    "192.168.1.4",
    "192.168.1.10",
    "192.168.1.11",
    "192.168.1.16",
    "192.168.1.17",
    "192.168.1.18",
    "192.168.1.19",
]

set_houston = set(set_houston)
set_atalanta = set(set_atalanta)
set_chicago = set(set_chicago)

print("Duplicate Houston and Atalanta")
print("-"*60)
print(set_houston & set_atalanta)
print("-"*60)
print("Duplicate All sites")
print("-"*60)
print(set_houston & set_atalanta & set_chicago)
print("-"*60)
print("Unique Chicago")
print("-"*60)
print(set_chicago.difference(set_atalanta).difference(set_houston))