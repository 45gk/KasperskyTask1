import platform
import subprocess
import re
import json


class PingAnalyzer:
    def __init__(self, host, count=4):
        self.host = host
        self.count = count
        self.results = self.ping()

    """Метод запускающий команду ping"""
    def ping(self):
        system = platform.system()
        if system == "Windows":
            output = subprocess.run(['ping', '-n', str(self.count), self.host], capture_output=True, text=True)
            result = output.stdout.encode('cp1251').decode('cp866')
        elif system == "Linux":
            output = subprocess.run(['ping', '-c', str(self.count), self.host], capture_output=True, text=True)
            result = output.stdout
        else:
            raise OSError("Unsupported operating system")

        print(result)
        if system == "Windows":
            min_time = re.search(r"Минимальное = (\d+)мсек", result)
            max_time = re.search(r"Максимальное = (\d+) мсек", result)
            avg_time = re.search(r"Среднее = (\d+) мсек", result)
            loss_rate = re.search(r'потеряно = (\d+)', result)
            # loss_rate = 0
        elif system == "Linux":
            min_time = re.search(r"min/avg/max/mdev = (\d+.\d+)/(\d+.\d+)/(\d+.\d+)/(\d+.\d+)", result)
            loss_rate = re.search(r"(\d+)% packet loss", result)
        print([min_time,max_time,avg_time,loss_rate])
        if min_time and max_time and avg_time and loss_rate:
            return {
                "min": int(min_time.group(1)),
                "max": int(max_time.group(1)),
                "avg": int(avg_time.group(1)),
                "loss_rate": int(loss_rate.group(1))
            }
        else:
            raise ValueError("Parsing error")


    """Метод для анализа """
    def analyze(self):
        if self.results["loss_rate"] > 0:
            print("Потери пакетов обнаружены")
            # Другие действия при потери пакетов

        jitter = self.results["max"] - self.results["min"]
        self.results["jitter"] = jitter

        return self.results

    """Метод для вывода результата в формате json"""
    def to_json(self):
        return json.dumps(self.results, indent=4)
