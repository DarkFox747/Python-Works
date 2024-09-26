import xlsxwriter
from bs4 import BeautifulSoup
import io
import os
import time
import sys

print("-- || MANIFIESTOS EXCEL V1 || --" + "\n")

excel_archivo = "./data/data.dat"

excel_rango = []

with open(excel_archivo) as f:
  excel_rango = f.read().splitlines()

inicial0 = excel_rango[0]
final0 = excel_rango[1]

inicial = int(inicial0)
final = int(final0)

disco = "./Excel/Manifiestos_"
dire = str(inicial) + "_a_" + str(final)
extension = ".xlsx"

os.system("cls")

print("Creando Planilla Excel")

dire_final = str(disco) + str(dire) + str(extension)
workbook = xlsxwriter.Workbook(dire_final)
worksheet = workbook.add_worksheet()

final_convertido = int(final) + 1
url_inicial = "./Descargas/Manifiesto_"
url_ext = ".html"

print("Creando Planilla Excel")
time.sleep(.05)
print("Decodificando Codec UTF-8")

for rango_manifiesto1 in range(inicial, final_convertido):
    url_numero1 = str(rango_manifiesto1)
    print("Decodificando Manifiesto: " + str(rango_manifiesto1), end='\r')
    sys.stdout.flush()
    with io.open(url_inicial + url_numero1 + url_ext, 'r', encoding='utf-8', errors="ignore") as f:
        text = f.read()
    with io.open(url_inicial + url_numero1 + url_ext, 'w', encoding='latin-1', errors="ignore") as f:
        f.write(text)

time.sleep(.05)
print('\n')
print("100%")

time.sleep(.05)
print("Escribiendo Archivo de Excel")

for rango_manifiesto in range(inicial, final_convertido):
    url_numero = str(rango_manifiesto)
    numero_salvaje = inicial - rango_manifiesto
    numero_chaman = -numero_salvaje
    url_final = str(url_inicial) + str(url_numero) + str(url_ext)
    print("Escribiendo: " + str(rango_manifiesto), end='\r')
    sys.stdout.flush()
    soup = BeautifulSoup(open(url_final), "html.parser")
    mylist = []
    mylist = soup.find_all('p')
    rangolista = len(mylist)
    for ranga in range(0, rangolista):
        rango = int(ranga)
        worksheet.write_row(numero_chaman, ranga, [mylist[rango].text])
workbook.close()

print('\n')
print("100%")
print("PROCESO FINALIZADO")