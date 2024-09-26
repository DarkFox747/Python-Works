import sqlite3
import csv

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('mi_base_de_datos.db')
cursor = conn.cursor()

# Crear una tabla con una clave compuesta única (modifica según tus necesidades)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS mi_tabla (
        Tipo_certificado TEXT,
        Estado TEXT,
        Fecha DATE,
        Manifiesto INTEGER,
        Generador TEXT,
        Cuit_Generador VARCHAR,
        ID_Generador INTEGER,
        Domicilio_Generador TEXT,
        Localidad_generador TEXT,
        Transportista TEXT,
        Cuit_Transportista TEXT,
        ID_Transportista INTEGER,
        Domicilio_Transportista TEXT,
        Localidad_Transportista TEXT,
        Operador TEXT,
        Cuit_Operador TEXT,
        ID_Operador INTEGER,
        Domicilio_Operador TEXT,
        Localidad_Operador TEXT,
        Tipo_Residuo VARCHAR,
        kilos_Residuo INTEGER,
        PRIMARY KEY (Manifiesto, Tipo_Residuo)
    )
''')

# Ruta al archivo CSV
ruta_csv = 'final/archivo_combinado_actualizado.csv'  # Reemplaza con la ruta a tu archivo CSV

# Abrir el archivo CSV y leer su contenido
with open(ruta_csv, 'r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # Obtener los nombres de las columnas del CSV si tiene cabecera
    cabecera = next(csvreader)
    
    # Preparar la consulta de inserción con OR IGNORE
    query = f'INSERT OR IGNORE INTO mi_tabla ({", ".join(cabecera)}) VALUES ({", ".join(["?" for _ in cabecera])})'
    
    for fila in csvreader:
        try:
            # Filtrar caracteres de control en la fila
            fila = [campo.replace('\x1a', '') for campo in fila]
            
            # Verificar si la fila está vacía
            if all(campo.strip() == '' for campo in fila):
                print(f"Fila vacía encontrada y omitida: {fila}")
                continue

            cursor.execute(query, fila)
        except sqlite3.Error as e:
            print(f"Error al insertar la fila {fila}: {e}")

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Datos insertados exitosamente en la base de datos.")
