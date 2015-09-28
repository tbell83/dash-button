#!/usr/bin/python
from scapy.all import *
from datetime import datetime


def arp_display(pkt):
    if pkt[ARP].op == 1:  # who-has (request)
        if pkt[ARP].psrc == '0.0.0.0':  # ARP Probe
            print "ARP Probe from: {0} at {1}".format(pkt[ARP].hwsrc,
                                                      str(datetime.now()))

print sniff(prn=arp_display, filter="arp", store=0)
