from scapy.all import *


class TrafficSniffer:
    def __init__(self, count=10):
        self.count = count

    def sniff_traffic(self):
        packets = sniff(count=self.count)
        return packets

    def show_packets(self, packets):
        for packet in packets:
            print(packet.summary())
