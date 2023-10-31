import socket
from urllib.request import urlopen
from Task import Ping
from Task import Sniffer

""" Метод для получения внешнего IP-адреса """
def get_public_ip():
    public_ip = urlopen('http://ip.42.pl/raw').read().decode('utf-8')
    return public_ip


# Пример использования классов из предыдущих частей
if __name__ == "__main__":
    # Получить локальный IP-адрес
    local_ip = socket.gethostbyname(socket.gethostname())
    print("Локальный IP-адрес:", local_ip)

    """Получение внешнего ip"""
    public_ip = get_public_ip()
    print("Внешний IP-адрес:", public_ip)

    '''Запуск пинга на несколько адресов '''
    hosts = ["google.com", "yahoo.com"]
    for host in hosts:
        analyzer = Ping.PingAnalyzer(host, count=4)
        print(f"Результаты пинга для {host}:")
        print(analyzer.analyze())

    ''' Перехват трафика от команды пинг '''
    sniffer = Sniffer.TrafficSniffer(count=10)
    captured_packets = sniffer.sniff_traffic()
    sniffer.show_packets(captured_packets)
