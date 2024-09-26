import os
import requests
from time import time as timer
from concurrent.futures import ThreadPoolExecutor as PoolExecutor
from urllib3.exceptions import InsecureRequestWarning
import sys

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

url = "https://sistemas.opds.gba.gov.ar/Establecimientos/Manifiesto/operador_resumenmanifiesto.php"

rangos = []

error_archivo = "./Faltantes.dat"
data_archivo = "./data.dat"

if os.path.exists(error_archivo) and os.path.getsize(error_archivo) > 0:
    with open(error_archivo) as f:
        rangos = f.read().splitlines()
else:
    print(" ")

def fetch_url(rango):
    data = {"hidmanifiesto": rango}
    r = requests.post(url, data, verify=False)
    r.raise_for_status()
    print("Descargando Manifiesto: " + str(rango), end='\r')
    sys.stdout.flush()

    file = open("../Descargas/Manifiesto_" + str(rango) + ".html", "w", encoding="utf-8")
    file.write(r.text)
    with open("../Descargas/Manifiesto_" + str(rango) + ".html", encoding="utf-8") as Manifest:
        if 'CERTIFICADO NRO' in Manifest.read():
            pass
        else:
            print("ERROR: ARCHIVO VACIO")
            os.rename("../Descargas/Manifiesto_" + str(rango) + ".html", "../Descargas/Manifiesto_" + str(rango) + "_empty" + ".html")
    file.close()

if rangos:
    print("Creando Array" + "\n")

    start = timer()

    with PoolExecutor(max_workers=10) as executor:
        for _ in executor.map(fetch_url, rangos):
            pass

    print("\n")
    print("Descarga Terminada" + "\n")
    print(f"Tiempo de Descarga: {timer() - start}")
else:
    print("No hay manifiestos faltantes para descargar.")
