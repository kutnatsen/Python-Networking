'''
Copy your solution from exercise3 to exercise4. Add an 'import pdb' and pdb.set_trace() statement outside of your function (i.e. where you have your function calls).
Inside of pdb, experiment with: 
⦁	Listing your code.
⦁	Using 'next' and 'step' to walk through your code. Make sure you understand the difference between next and step.
⦁	Experiment with 'up' and 'down' to move up and down the code stack.
⦁	Use p <variable> to inspect a variable.
⦁	Set a breakpoint and run your code to the breakpoint.
⦁	Use '!command' to change a variable (for example !new_mac = [])
'''
import pdb

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
    breakpoint()
    return new_mac


print(mac_conv("0000.aaaa.bbbb"))
