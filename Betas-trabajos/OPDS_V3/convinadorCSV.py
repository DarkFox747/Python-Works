
#Con esto convinamos todos los csv de la carpeta CSV
import os
import subprocess
import pandas as pd
# Ruta de la carpeta donde se encuentran los archivos CSV
ruta_carpeta_csv = 'CSV'  # Reemplaza esto con la ruta correcta
ruta_guardar_combinado = 'combinedCSV'
# Comando para Windows
comando_windows = f'copy "{ruta_carpeta_csv}\\*.csv" "{ruta_guardar_combinado}\\combined.csv"'

# Comando para Linux/Mac
comando_linux = f'cat "{ruta_carpeta_csv}/*.csv" > "{ruta_guardar_combinado}/combined.csv"'


# Verifica el sistema operativo
import platform
sistema_operativo = platform.system()

# Ejecuta el comando según el sistema operativo
if sistema_operativo == 'Windows':
    subprocess.run(comando_windows, shell=True)
else:
    subprocess.run(comando_linux, shell=True)

print("Archivos CSV combinados exitosamente.")

print("Agregando titulos")

ruta_csv_combinado = 'combinedCSV/combined.csv'
# Leer el archivo CSV combinado
df_combinado = pd.read_csv(ruta_csv_combinado)

# Definir los títulos de las columnas
títulos_columnas = [
    'Tipo_certificado', 'Estado', 'Fecha', 'Manifiesto', 'Generador', 'Cuit_Generador', 'ID_Generador', 'Domicilio_Generador', 'Localidad_Generador',
    'Transportista', 'Cuit_Transportista', 'ID_Transportista', 'Domicilio_Transportista', 'Localidad_Transportista',
    'Operador', 'Cuit_Operador', 'ID_Operador', 'Domicilio_Operador', 'Localidad_Operador', 'Tipo_Residuo', 'kilos_Residuo'
]

df_combinado.columns = títulos_columnas

# Guardar el DataFrame con los títulos en un nuevo archivo CSV
ruta_csv_combinado_actualizado = 'final/archivo_combinado_actualizado.csv'  # Ruta para guardar el archivo actualizado
df_combinado.to_csv(ruta_csv_combinado_actualizado, index=False, header=True)    

print(f"Títulos agregados exitosamente al archivo CSV en {ruta_csv_combinado_actualizado}")