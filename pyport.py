#!/usr/bin/python
import nmap
import sys
from pyfiglet import Figlet
logo = Figlet(font='graffiti')
print(logo.renderText('Pyport Scanner'))

#argument validator
if len(sys.argv) != 2:
    host = input("Enter the name of host:\n")
    print("Usage : python pyport.py [ip_address]")
    print("Example : python pyport.py 192.168.0.1")
    sys.exit("Plese provide one argument!")

nm_scan = nmap.PortScanner()
print('\nPyport Running...\n')
nm_scanner = nm_scan.scan(sys.argv[1],'22,80,25,53',arguments='-O')

host_is_up = "The host is: "+nm_scanner['scan'][sys.argv[1]]['status']['state']+".\n"

port_open = "The port 80 is: "+nm_scanner['scan'][sys.argv[1]]['tcp'][80]['state']+".\n"

method_scan = "This method of scanning is: "+nm_scanner['scan'][sys.argv[1]]['tcp'][80]['reason']+".\n"




