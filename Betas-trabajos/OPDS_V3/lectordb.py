import sqlite3

def count_rows_and_show_data(db_name, table_name, num_rows=5):
    try:
        # Conectar a la base de datos
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Contar el número de filas en la tabla especificada
        cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
        row_count = cursor.fetchone()[0]

        print(f"El número de filas en la tabla '{table_name}' es: {row_count}")

        # Mostrar las primeras filas de la tabla
        cursor.execute(f"SELECT * FROM {table_name} LIMIT {num_rows};")
        rows = cursor.fetchall()

        print(f"\nLas primeras {num_rows} filas de la tabla '{table_name}' son:")
        for row in rows:
            print(row)

        # Cerrar la conexión
        cursor.close()
        conn.close()

    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos: {e}")

# Llamar a la función con el nombre de la base de datos, el nombre de la tabla y el número de filas a mostrar
count_rows_and_show_data('mi_base_de_datos.db', 'mi_tabla', num_rows=10)
