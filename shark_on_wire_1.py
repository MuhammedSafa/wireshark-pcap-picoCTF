#!/usr/bin/env python3

from scapy.all import *

pcap = rdpcap("capture.pcap")
flag=[]
for p in pcap[UDP]:
    try:
        if(p[IP].src=="10.0.0.2" and (p[IP].dst=="10.0.0.12" or p[IP].dst=="10.0.0.13")):
            #p.show()
            flag.append(p[Raw].load.decode("utf-8"))
    except:
            continue

print("".join(flag))
