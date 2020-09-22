import socket
import os
import json
import subprocess
import time
from datetime import datetime

# Vars
netid = '192.168.20.'
netmask = '24'
global iplst
iplst = []
alive = []
logging = False

if netmask == '24':
    netrange = '255'

class eventStream:
    # Logging class object
    def outCons(msg):
        # prints log to console
        print('[datetime.now()]::[' + msg + ']')
    def outFile(msg):
        # Prints log to log file
    def log(msg):
        if logging = True:
            outCons(msg)
        else:
            outFile(msg)    



def main():
    # print("[+]: Generating the host list")
    eventStream.log("Generating the host list")
    for i in range(1, int(netrange)):
        ip = netid + str(i)
        iplst.append(ip)
    print("[+]: IP list contains " + str(len(iplst)) + " hosts")
    scanner(iplst)


def scanner(iplst):
    t1 = datetime.now()
    for i in iplst:
        currentip = i
        getalive(currentip, iplst)
        print("[+]: Found " + str(len(alive)) + " alive hosts")
    t2 = datetime.now()
    time = t2 - t1
    print("[?]: Scan took [" + str(time) + "] to scan " + str(len(iplst)) + " hosts")


def getalive(currentip, iplst):
    # print("[*]: Scanning " + str(currentip))
    test = subprocess.call(['ping', '-n', '1', currentip])
    if test == '0':
        alive.append(currentip)
        print("[+]: " + currentip + " is alive")
    elif test == '1':
        print("[!]: Host isnt alive")

def scan(currentip):
    print("")    

def getbanner(currentip):
    print("[*]: Getting banner for" + currentip)


main()
