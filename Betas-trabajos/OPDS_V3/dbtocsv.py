import sqlite3
import csv
import os

# Establecer la conexión a la base de datos
conn = sqlite3.connect('mi_base_de_datos.db')
cursor = conn.cursor()

# Consulta SQL para obtener todos los datos de una tabla (reemplaza 'nombre_tabla' por el nombre real de tu tabla)
query = "SELECT * FROM mi_tabla;"

# Ejecutar la consulta y obtener los resultados
cursor.execute(query)
results = cursor.fetchall()

# Cerrar la conexión a la base de datos
conn.close()


# Guardar los resultados en un archivo CSV en la carpeta 'carpeta_final'
csv_path = 'final/datos.csv'
with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    # Escribir los nombres de las columnas como encabezados del CSV
    csv_writer.writerow([description[0] for description in cursor.description])
    # Escribir los datos en el CSV
    csv_writer.writerows(results)

print(f"Los datos se han exportado correctamente a '{csv_path}'.")