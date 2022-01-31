'''
Similar to lesson3, exercise4 write a function that normalizes a MAC address to the following format:
01:23:45:67:89:AB
This function should handle the lower-case to upper-case conversion.
It should also handle converting from '0000.aaaa.bbbb' and from '00-00-aa-aa-bb-bb' formats.
The function should have one parameter, the mac_address. It should return the normalized MAC address
Single digit bytes should be zero-padded to two digits. In other words, this:
a:b:c:d:e:f
should be converted to:
0A:0B:0C:0D:0E:0F
Write several test cases for your function and verify it is working properly.
'''

def mac_conv(mac):
    mac_addr = mac.upper()
    new_mac = []
    if "." in mac_addr:
        while len(mac_addr) > 0:
            mac_addr = mac_addr.replace(".","")
            entry = mac_addr[:2]
            mac_addr = mac_addr[2:]
            new_mac.append(entry)
        new_mac = ":".join(new_mac)
    elif ":" in mac_addr:
        octs = mac_addr.split(":")
        for oct in octs:
            if len(oct) < 2:
                oct = "0" + oct
            new_mac.append(oct)
        new_mac = ":".join(new_mac)
    elif "-" in mac_addr:
        mac_addr = mac_addr.replace("-",":")
        octs = mac_addr.split(":")
        for oct in octs:
            if len(oct) < 2:
                oct = "0" + oct
            new_mac.append(oct)
        new_mac = ":".join(new_mac)
    return new_mac


print(mac_conv("0000.aaaa.bbbb"))
print("-" *80)
print(mac_conv("a:b:c:d:e:f"))
print("-" *80)
print(mac_conv("00-00-aa-aa-bb-bb"))
print("-" *80)
print(mac_conv("04-10-a-aa-b-b"))

