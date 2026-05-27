import socket
import ipaddress
from tqdm import tqdm
from menu import RESULT_FILE

def validation_ip ():
    while True:
        ip = input("Enter IP: ")
        try:
            ipaddress.ip_address(ip)
            return ip
        except ValueError:
            print("Invalid IP. Please try again.")


def validation_port():
    while True:
        try:
            port_range = int(input("Enter the port range (1 - 65535): "))
            if 0 < port_range < 65536:
                return port_range
            else:
                print("Out of range")
        except ValueError:
            print("ERROR")

             
def scan (ip, port_range):
    with open(RESULT_FILE, "w") as archivo:
        pass
    
    for port in tqdm(range(1, port_range + 1), desc = "scanning", unit = "Ports"):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        target = (ip, port)
        result = sock.connect_ex(target)

        try:
            service = socket.getservbyport(port, 'tcp')
            if result == 0:
                with open("scan results.txt", "a") as archivo:
                    print(f"{port}:{service} OPEN", file =archivo)        
        except OSError:
            continue 
        
        sock.close()  
    print("SCANNED PORTS")