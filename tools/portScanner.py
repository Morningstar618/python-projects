#!/bin/python3

import sys
import socket
from datetime import datetime

ERROR = "[-]"   
OK = "[+]"
INFO = "[*]"

# Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4
else:
    print(f" {ERROR} Invalid Syntax")
    print(f" {INFO} Syntax: python3 portScanner.py <ip>")

# Add a pretty banner
print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f" {INFO} Port {port} is open")
        s.close()
except KeyboardInterrupt:
    print(f"\n {INFO} Exiting program.")
    sys.exit()
except socket.gaierror:
    print(f" {ERROR} Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print(f" {ERROR} Could not connect to server.")