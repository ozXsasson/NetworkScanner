#!/usr/bin/env python

import scapy.all as scapy
import argparse

def getArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range.")
    options = parser.parse_args()
    return options
def scan(ip):
    arpRequest = scapy.ARP(pdst=ip)
    arpBroadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_Request_Broadcast = arpBroadcast/arpRequest
    arp_AnswerdList = scapy.srp(arp_Request_Broadcast, timeout=1, verbose=False)[0]

    clientsList = []
    for element in arp_AnswerdList:
        clientDict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clientsList.append(clientDict)

    return clientsList

def printResult(resultsList):
    print("IP\t\tMAC Adress\n-----------------------------------")
    for client in resultsList:
        print(client["ip"] + "\t" + client["mac"])

optIP = getArguments()
scanResult = scan(optIP.target)
printResult(scanResult)