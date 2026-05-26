import socket
import ipaddress
from tqdm import tqdm

def validacion_ip ():
    while True:
        ip = input("Ingrese IP: ")
        try:
            ipaddress.ip_address(ip)
            return ip
        except ValueError:
            print("IP invalida, intente denuevo")



def validacion_puerto():
    while True:
        try:
            rango_de_puerto = int(input("Ingrese el rango de puertos (1 - 65535): "))
            if 0 < rango_de_puerto < 65536:
                return rango_de_puerto
            else:
                print("Fuera de rango")
        except ValueError:
            print("ERROR")

             
def escaneo (ip, rango_de_puerto):
    for puerto in tqdm(range(1, rango_de_puerto + 1), desc = "Escaneando", unit = "Puertos"):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        target = (ip, puerto)
        resultado = sock.connect_ex(target)

        try:
            servicio = socket.getservbyport(puerto, 'tcp')
            if resultado == 0:
                with open("resultado_escaneo.txt", "a") as archivo:
                    print(f"{puerto}:{servicio} ABIERTO ", file =archivo)        
        except OSError:
            continue 
        
        sock.close()  
    print("PUERTOS ESCANEADOS")