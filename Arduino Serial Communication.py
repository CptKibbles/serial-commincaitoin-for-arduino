# Importing Libraries
import serial
import time
import serial.tools.list_ports


ports = list(serial.tools.list_ports.comports())
# List_ports = ''.join(str(x) for x in ports)

for p in ports:
    if 'Arduino' in p.manufacturer:
        print (p.device)
    else:
        print ("no arduino found")