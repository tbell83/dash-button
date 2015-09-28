#!/usr/bin/python
import commands, re

PREFIX = "192.168.1" #Network prefix
MIN = "0" #Starting network address, eg 192.168.1.0
MAX = "12" #Closing network address, e.g. 192.168.1.55
results = []

while 1:
    new = commands.getoutput('for i in {'+MIN+'..'+MAX+'}; do ping -c 1 -t 1 '+PREFIX+'.$i | grep "from"; done') #Ping sweep the network to find connected devices
    tmp = re.findall(PREFIX+"\.(\d+)", str(new)) #Pull out IP addresses from the ping results
    if tmp != results:
        for t in tmp:
            if t not in results:
                print "New device at" + PREFIX + "." + str(t)
            results = tmp