from Escaner_de_puerto import validation_ip, validation_port, scan

RESULT_FILE = "scan_results.txt"

def show_results():
    try:
        with open(RESULT_FILE, "r") as archivo:
            print("\n--- RESULTADOS DEL ESCANEO ---")
            print(archivo.read())
    except FileNotFoundError:
        print("No se han encontrado resultados de escaneo.")

def main():
    while True:
        print("\n--- PORT SCANNER ---")
        print("1. Escanear")
        print("2. Ver resultados")
        print("3. Salir")

        option = input("Seleccione una opción: ")

        match option:
            case "1":
                ip = validation_ip()
                port_range = validation_port()
                scan(ip, port_range)
            case "2":
                show_results()
            case "3":
                print("saliendo...")
                break
            case _:
                print("Opción inválida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()