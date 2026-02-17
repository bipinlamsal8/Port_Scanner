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

def scan_single_port(target, port, timeout=1.0): # this function is used to scan a single port and return the status and service information
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((target, port))

            try:
                service = socket.getservbyport(port)
            except OSError:
                service = "unknown"

            if result == 0:
                return "OPEN", service
            else:
                return "CLOSED", service

    except socket.timeout:
        return "FILTERED", "unknown"
    except socket.error:
        return "ERROR", "unknown"

def scan_port_range(target, start_port, end_port): # this function is used to scan a range of ports and return the results as a list of PortResult objects
    results = []

    print("\n" + "=" * 50)
    print(f"Scanning {target} from port {start_port} to {end_port}")
    print("=" * 50)

    start_time = time.time()

    for port in range(start_port, end_port + 1):
        status, service = scan_single_port(target, port)
        result = PortResult(port, status, service, time.time())
        results.append(result)

        if status == "OPEN":
            print(f"[+] {result.display()}")

    end_time = time.time()
    duration = end_time - start_time

    print("\nScan Complete")
    print(f"Total ports scanned: {len(results)}")
    print(f"Scan duration: {duration:.2f} seconds")

    return results


def main(): #CLI for port scannerr
    print("=" * 50)
    print("        NETWORK PORT SCANNER")
    print("=" * 50)