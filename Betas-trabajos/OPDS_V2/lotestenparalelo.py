import os
import pandas as pd
from scritp4 import *
from threading import Thread, Lock
from queue import Queue

# Definir las columnas del DataFrame
columnas = [
    'Tipo_certificado', 'Estado', 'Fecha', 'Manifiesto', 'Generador', 'Cuit_Generador', 'ID_Generador', 
    'Domicilio_Generador', 'Localidad_Generador', 'Transportista', 'Cuit_Transportista', 'ID_Transportista', 
    'Domicilio_Transportista', 'Localidad_Transportista', 'Operador', 'Cuit_Operador', 'ID_Operador', 
    'Domicilio_Operador', 'Localidad_Operador', 'Tipo_Residuo', 'kilos_Residuo'
]

# Carpeta donde se encuentran los archivos HTML
carpeta = "Descargas2"
archivos_txt = [archivo for archivo in os.listdir(carpeta) if archivo.endswith('.html')]

# Tamaño del lote
tamano_lote = 1000  # Ajusta según sea necesario
lock = Lock()

def procesar_lote(lote, numero_lote):
    datos = []
    
    for archivo in lote:
        ruta_archivo = os.path.join(carpeta, archivo)
        if os.path.exists(ruta_archivo):
            try:
                # Abre el archivo en modo lectura ('r')
                with open(ruta_archivo, 'r', encoding='utf-8') as archivo_txt:
                    # Lee y muestra el contenido del archivo
                    contenido = archivo_txt.read()
                    soup = parse_html(contenido)

                    # Extraer datos
                    try:
                        tipo_certificado = extraer_destino_residuo(soup)
                        tipo_certificado = "Operacion" if tipo_certificado == "Disposicion Final" else "Tratamiento"
                        fecha = extraer_fecha(soup)
                        numero = extraer_numero(soup)
                        generador = extraer_razon_social(soup)
                        transportista = extraer_razon_social_transportista(soup)
                        operador = extraer_razon_social_destino(soup)
                        tipoResiduo = extraer_categoria_y_cantidad(soup)
                        kilosResiduo = kilos(soup)
                        cuits, ids = extraer_cuits(soup)
                        domicilios = extraer_domicilios(soup)
                        localidades = extraer_localidad(soup)
                        estado = encontrar_estado(soup)
                    except Exception as e:
                        print(f"Error al extraer datos del archivo {ruta_archivo}: {e}")
                        continue

                    for j in range(len(tipoResiduo)):
                        try:
                            # Agregar datos a la lista
                            datos.append([
                                tipo_certificado, estado, fecha, numero, generador, cuits[0], ids[0], domicilios[0], localidades[0],
                                transportista, cuits[1], ids[1], domicilios[1], localidades[1],
                                operador, cuits[2], ids[2], domicilios[2], localidades[2], tipoResiduo[j], kilosResiduo[j]
                            ])
                        except Exception as e:
                            print(f"Error al procesar datos del archivo {ruta_archivo}: {e}")

            except Exception as e:
                print(f"Error al procesar el archivo {ruta_archivo}: {e}")

    # Crear DataFrame desde la lista de datos
    df = pd.DataFrame(datos, columns=columnas)

    # Asegurar que la carpeta CSV existe
    os.makedirs('CSV', exist_ok=True)

    # Generar el nombre del archivo CSV para el lote
    nombre_archivo = f'CSV/lote_{numero_lote}.csv'

    # Guardar el DataFrame en un archivo CSV sin el encabezado
    try:
        with lock:
            df.to_csv(nombre_archivo, index=False, header=False)  
        print(f"Archivo guardado como {nombre_archivo}")
    except Exception as e:
        print(f"Error al guardar el archivo CSV: {e}")

def worker(queue):
    while not queue.empty():
        lote, numero_lote = queue.get()
        procesar_lote(lote, numero_lote)
        queue.task_done()

def main():
    # Dividir archivos en lotes
    lotes = [archivos_txt[i:i + tamano_lote] for i in range(0, len(archivos_txt), tamano_lote)]

    queue = Queue()
    for i, lote in enumerate(lotes):
        queue.put((lote, i + 1))

    # Crear y lanzar los hilos
    threads = []
    for _ in range(min(10, queue.qsize())):  # Ajusta el número de hilos según sea necesario
        thread = Thread(target=worker, args=(queue,))
        thread.start()
        threads.append(thread)

    # Esperar a que todos los hilos terminen
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()
