from scapy.all import *

flag = []

packets = rdpcap('capture.pcap')
for packet in packets:
    if UDP in packet and packet[UDP].dport == 22:
        flag.append(chr(packet[UDP].sport - 5000))
print("".join(flag))
