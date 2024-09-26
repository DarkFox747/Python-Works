import os
import time

def main_menu():
    print("-- OPERADOR DE MANIFIESTOS V8 --")
    print()
    print("1. Descargador de Manifiestos")
    print("2. Comprobar y descargar faltantes")
    print("3. Crear EXCEL (con todos los manifiestos guardados)")
    
    print("5. Salir")
    print()
    choice = input("Introduzca el número para elegir opción: ").strip()

    if choice == '1':
        descarga()
    elif choice == '3':
        excel()
    elif choice == '2':
        faltantes()
    elif choice == '5':
        end()
    else:
        print(f'"{choice}" opción no válida, intente de nuevo')
        print()
        main_menu()

def descarga():
    print("DESCARGA")
    os.system("python3 scrape.py")
    main_menu()

def excel():
    print("EXCEL")    
    os.system("python3 createExcel_v4.py")
    time.sleep(1)
    os.system('cls')
    main_menu()

def faltantes():
    print("FALTANTES")
    os.chdir("data")
    os.system("python3 dic.py")
    os.system("python3 scrape_faltantes.py")
    os.chdir("..")
    main_menu()

def end():
    print("Saliendo...")
    exit()

if __name__ == "__main__":
    main_menu()
