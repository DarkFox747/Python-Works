import os

path_archivotext = './Faltantes.dat'
path_archivodata = './data.dat'

try:
  os.remove(path_archivotext)
except:
  pass

try:
  os.remove(path_archivodata)
except:
  pass


print("-- || DICCIONARIO DE MANIFIESTOS FALTANTES || --" + "\n")
rangoinicio = input("RANGO INICIAL: ")
rangofinal = input("RANGO FINAL: ")

rangofinal2 = int(rangofinal) + 1
rangoinicio1 = int(rangoinicio)

escribir_data = open(path_archivodata, 'a')
escribir_data.write(str(rangoinicio))
escribir_data.write('\n')
escribir_data.write(str(rangofinal))

print("Procesando")

for rango in range(rangoinicio1, rangofinal2):
    try:
        old_file = "../Descargas/Manifiesto_" + str(rango) + ".html"
        with open(old_file) as Manifest:
            if 'CERTIFICADO NRO' in Manifest.read():
                print("Ya encontrado: ", str(rango))
    except:
        try:
            print("Escribiendo Faltante")
            error = open(path_archivotext, 'a')
            error.write(str(rango))
            error.write('\n')
        except:
            pass
        pass

print("100%")
print("PROCESO TERMINADO")