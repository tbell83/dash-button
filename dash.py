from scapy.all import *
import requests
import time

def arp_display(pkt):
#  print 'IP: {0}'.format(pkt[ARP].psrc)
#  print 'MAC: {0}'.format(pkt[ARP].hwsrc)

  timestamp = time.strftime("%Y-%m-%d %H:%M")
  if pkt[ARP].op == 1: #who-has (request)
    if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
      if pkt[ARP].hwsrc == '00:bb:3a:cc:77:b4':
	print 'Hey, it\'s me, your Tide button!'
      else:
        print "ARP Probe from unknown device: " + pkt[ARP].hwsrc

while True:
  print sniff(prn=arp_display, filter="arp", store=0)
