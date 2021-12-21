'''
Create a list of five IP addresses.
Use the .append() method to add an IP address onto the end of the list. 
Use the .extend() method to add two more IP addresses to the end of the list.
Use list concatenation to add two more IP addresses to the end of the list.
Print out the entire list of ip addresses. 
Print out the first IP address in the list. 
Print out the last IP address in the list.
Using the .pop() method to remove the first IP address in the list and the last IP address in the list.
Update the new first IP address in the list to be '2.2.2.2'. 
Print out the new first IP address in the list.
'''


ip_list = ["1.1.1.1","10.10.10.10","100.100.100.100","50.50.50.50","30.30.30.30"]
ip_list.append("40.40.40.40")
ip_list.extend(["60.60.60.60","70.70.70.70"])
ip_list = ip_list + ["80.80.80.80", "90.90.90.90"]
print(ip_list)

print(ip_list[0])
print(ip_list[-1])

first_ip = ip_list.pop(0)
last_ip = ip_list.pop(-1)

ip_list[0] = "2.2.2.2"
print(ip_list[0])
