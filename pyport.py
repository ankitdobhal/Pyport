#!/usr/bin/python
import nmap
import sys

host = input("Enter target name:")
if host:
    print("Usage : python3 autoscanner.py [ip_address]")
    print("Example : python3 autoscanner.py 192.168.0.1")

nm_scan = nmap.PortScanner()
nm_scanner = nm_scan.scan(sys.argv[1],'22,80,25,53',arguments='-O')
print(nm_scanner)

