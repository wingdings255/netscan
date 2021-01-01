#!/bin/env python3
# import os
# import json
import socket
import ipcalc
import subprocess
import time

# Vars
netid = '192.168.1.0/24'  # For testing
ports = ['20', '22', '21', '80', '443']
global iplst
iplst = []
alive = []


def main():
    iplst = ipcalc.Network(netid)
    print("[+]:: IP list contains " + str(len(iplst)) + " hosts")
    t1 = time.time()
    for i in iplst:
        getAlive(i)
    t2 = time.time()
    tEnd = t2 - t1
    t = round(tEnd, 3)
    print("[!]:: Scan took " + str(t) + " seconds")
    print("[+]:: Found " + str(len(alive)) + "/" + str(len(iplst)) + " alive hosts")


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


def scanner(host):
    addr = str(host)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for i in ports:
        s.connect(addr, i)



main()
