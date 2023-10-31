from Task import Ping
from Task import Sniffer

if __name__ == "__main__":
    """ Выполнение 1 части """
    analyzer = Ping.PingAnalyzer("google.com", count=4)
    print(analyzer.analyze())
    print(analyzer.to_json())

    """ Выполнение 2 части """
    sniffer = Sniffer.TrafficSniffer(count=10)
    captured_packets = sniffer.sniff_traffic()
    sniffer.show_packets(captured_packets)