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

def validate_ip(ip_address): # ip address is validated using this function
     
    parts = ip_address.split(".")
    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False

    return True


def validate_port(port): # port number is validated using this function
    return 1 <= port <= 65535