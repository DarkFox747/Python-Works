import pandas as pd
import os

# Define paths for CSV and Excel folders
ruta_csv = 'CSV/'
ruta_excel = 'Excel/'

# List CSV files
archivos_csv = os.listdir(ruta_csv)
datos_totales = pd.DataFrame()

# Define Excel header columns
columnas = [
    'Tipo_certificado', 'Estado', 'Fecha', 'Manifiesto', 'Generador', 'Cuit_Generador', 'ID_Generador',
    'Domicilio_Generador', 'Localidad_Generador', 'Transportista', 'Cuit_Transportista', 'ID_Transportista',
    'Domicilio_Transportista', 'Localidad_Transportista', 'Operador', 'Cuit_Operador', 'ID_Operador',
    'Domicilio_Operador', 'Localidad_Operador', 'Tipo_Residuo', 'kilos_Residuo'
]

for archivo in archivos_csv:
    counter = 1
    if archivo.endswith('.csv'):
        ruta_completa = os.path.join(ruta_csv, archivo)

        try:
            # Attempt to read the CSV file using error handling
            datos_csv = pd.read_csv(ruta_completa)
            datos_totales = pd.concat([datos_totales, datos_csv])            
        except pd.errors.EmptyDataError:
            # Handle the case of an empty CSV file
            print(f"Skipping empty file: {archivo}")
        print(counter)
        counter = counter+1

# Save the combined data to Excel if there's any data
if not datos_totales.empty:
    ruta_excel_completa = os.path.join(ruta_excel, 'Datos_totales.xlsx')
    datos_totales.to_excel(ruta_excel_completa, index=False, columns=columnas)
else:
    print("No data found in any CSV files. Excel file not created.")
