'''
Prompt a user to enter in an IP address from standard input. 
Read the IP address in and break it up into its octets. 
Print out the octets in decimal, binary, and hex.
Your program output should look like the following:

Please enter an IP address: 80.98.100.240
    Octet1         Octet2         Octet3         Octet4     
------------------------------------------------------------
      80             98             100            240      
   0b1010000      0b1100010      0b1100100     0b11110000   
     0x50           0x62           0x64           0xf0      
------------------------------------------------------------

Four columns, fifteen characters wide, a header column, data centered in the column.
'''

ip_addr = input("Enter IP Address: ")
octets = ip_addr.split(".")


print("{:^15}{:^15}{:^15}{:^15}".format("Octet1", "Octet2", "Octet3", "Octet4"))
print("-" * 60)
print("{:^15}{:^15}{:^15}{:^15}".format(octets[0], octets[1], octets[2], octets[3],))
print("{:^15}{:^15}{:^15}{:^15}".format(bin(int(octets[0])),bin(int(octets[1])),bin(int(octets[2])),bin(int(octets[3]))))
print("{:^15}{:^15}{:^15}{:^15}".format(hex(int(octets[0])),hex(int(octets[1])),hex(int(octets[2])),hex(int(octets[3]))))
print("-" * 60)
