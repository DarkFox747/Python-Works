import os
from scritp4 import*
import pandas as pd
import sqlite3
from dbManipu4 import *

# Definir las columnas del DataFrame
columnas = [
    'Tipo_certificado', 'Estado', 'Fecha', 'Manifiesto', 'Generador', 'Cuit_Generador', 'ID_Generador', 
    'Domicilio_Generador', 'Localidad_Generador', 'Transportista', 'Cuit_Transportista', 'ID_Transportista', 
    'Domicilio_Transportista', 'Localidad_Transportista', 'Operador', 'Cuit_Operador', 'ID_Operador', 
    'Domicilio_Operador', 'Localidad_Operador', 'Tipo_Residuo', 'kilos_Residuo'
]

# Carpeta donde se encuentran los archivos HTML
carpeta = "Descargas"
archivos_txt = [archivo for archivo in os.listdir(carpeta) if archivo.endswith('.html')]

# Crear conexión a la base de datos
try:
    conn = sqlite3.connect('localDB')
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
    exit()

# Procesar cada archivo HTML
for archivo in archivos_txt:
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

                for i in range(len(tipoResiduo)):
                    try:
                        # Insertar datos en la base de datos
                        insertDB(
                            tipo_certificado, estado, fecha, numero, generador, cuits[0], ids[0], domicilios[0], localidades[0],
                            transportista, cuits[1], ids[1], domicilios[1], localidades[1],
                            operador, cuits[2], ids[2], domicilios[2], localidades[2], tipoResiduo[i], kilosResiduo[i]
                        )
                    except Exception as e:
                        print(f"Error al insertar datos del archivo en la db {ruta_archivo}: {e}")

        except Exception as e:
            print(f"Error al procesar el archivo {ruta_archivo}: {e}")

# Commit y cierre de la conexión a la base de datos
try:
    conn.commit()
    conn.close()
except Exception as e:
    print(f"Error al cerrar la base de datos: {e}")

# Crear DataFrame desde la base de datos
try:
    conn = sqlite3.connect('localDB')
    sql = pd.read_sql('''SELECT * FROM data''', conn)
    df = pd.DataFrame(sql, columns=columnas)
    conn.close()
except Exception as e:
    print(f"Error al leer de la base de datos: {e}")

# Generar el nombre del archivo Excel
numero_archivo = 1
while os.path.exists(f'examples_{numero_archivo}.xlsx'):
    numero_archivo += 1

nombre_archivo = f'examples_{numero_archivo}.xlsx'
nombre_archivo = os.path.join('Excel', nombre_archivo)

# Guardar el DataFrame en un archivo Excel
try:
    df.to_excel(nombre_archivo, index=False)  
    print(f"Archivo guardado como {nombre_archivo}")
except Exception as e:
    print(f"Error al guardar el archivo Excel: {e}")
