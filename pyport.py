#!/usr/bin/python
import nmap
import sys

#argument validator
if len(sys.argv) != 2:
    sys.exit("Please provide one argument!")

host = input("Enter target name:")
if host:
    print("Usage : python3 autoscanner.py [ip_address]")
    print("Example : python3 autoscanner.py 192.168.0.1")

nm_scan = nmap.PortScanner()
print('\nRunning...\n')
nm_scanner = nm_scan.scan(sys.argv[1],'22,80,25,53',arguments='-O')

host_is_up = "The host is: "+nm_scanner['scan'][sys.argv[1]]['status']['state']+".\n"

port_open = "The port 80 is: "+nm_scanner['scan'][sys.argv[1]]['tcp'][80]['state']+".\n"

method_scan = "This method of scanning is: "+nm_scanner['scan'][sys.argv[1]]['tcp'][80]['reason']+".\n"

guessed_os = "There is a %s percent chance that the host is running %s"%(nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['accuracy'],nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['name'])+".\n"




