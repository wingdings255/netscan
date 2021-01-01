# import socket
# import os
# import json
import ipcalc
import subprocess
from datetime import datetime

# Vars
netid = '192.168.1.0/24'  # For testing
global iplst
iplst = []
alive = []


def main():
    iplst = ipcalc.Network(netid)
    print("[+]:: IP list contains " + str(len(iplst)) + " hosts")
    t1 = datetime.now()
    for i in iplst:
        getAlive(i)
    t2 = datetime.now()
    time = t2 - t1
    print("[!]:: Scan took " + time)


# Tests to see if host is alive with ping
def getAlive(host):
    addr = str(host)
    print("[+]:: Checking " + addr, end='-->STATUS::[')
    test = subprocess.call(['ping', '-c', '1', addr], stdout=subprocess.DEVNULL)
    if test == 0:
        alive.append(host)  # NOTE: Saved as [IP('192.168.0.1'),]
        print(" ALIVE ]")
    elif test == 1:
        print(" DEAD ]")


main()
