# simple inquiry example

import bluetooth

nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("found %d device(s)" % len(nearby_devices))

for addr, name in nearby_devices:
    print("  %s - %s" % (addr, name))

    selected_device = raw_input ("\n\n Select device: ")
    if  nearby_devices == selected_device:
        print ("Connected "+ addr)
