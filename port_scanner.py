import socket
import time 


class PortResult:
    # result of port scanner is stored in this keyword class
    
    def __init__(self, port, status, service, timestamp):
        self.port = port
        self.status = status
        self.service = service
        self.timestamp = timestamp

    def display(self):
        time_str = time.strftime('%H:%M:%S', time.localtime(self.timestamp))
        return f"Port {self.port} ({self.service}) : {self.status} - Scanned at {time_str}"