import os
import time

def main_menu():
    print("-- OPERADOR DE MANIFIESTOS  --")
    print()
    print("1. Descargador de Manifiestos")
    print("2. Comprobar y descargar faltantes")
    print("3. Crear CSV (descargados recientes)")
    print("4. Actualizar la Base de datos")
    print("5. Imprimir todos los datos en CSV de la base de datos")
    print("10. Salir")
    
    print()
    choice = input("Introduzca el número para elegir opción: ").strip()

    if choice == '1':
        descarga()
    elif choice == '3':
        excel()
    elif choice == '2':
        faltantes()
    elif choice == '4':
        db()
    elif choice=='5':
        imprimirdb()
    elif choice == '10':
        end()
    else:
        print(f'"{choice}" opción no válida, intente de nuevo')
        print()
        main_menu()

def descarga():
    print("DESCARGA")
    os.system("python3 scrape2.py")
    main_menu()

def excel():
    print("CSV")    
    #os.system("python3 createExcel_v4.py")
    os.system("python3 lotestenparalelo.py")
    os.system("python3 convinadorCSV.py")
    time.sleep(1)
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

def db():
    print("Acutualizando la base de datos...")
    os.system("python3 csvtodb.py")
    main_menu()

def imprimirdb():
    print("Imprimiendo base de datos...")
    os.system("python3 dbtocsv.py")
    main_menu()

if __name__ == "__main__":
    main_menu()
