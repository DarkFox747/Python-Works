import os
from scritp4 import*
import pandas as pd
import sqlite3
from dbManipu4 import*

columnas = ['Tipo_certificado','Estado', 'Fecha', 'Manifiesto', 'Generador','Cuit_Generador','ID_Generador','Domicilio_Generador','Localidad_Generador',
             'Transportista','Cuit_Transportista','ID_Transportista','Domicilio_Transportista','Localidad_Transportista', 
             'Operador','Cuit_Operador','ID_Operador','Domicilio_Operador','Localidad_Operador', 'Tipo_Residuo', 'kilos_Residuo']
#df = pd.DataFrame(columns=columnas)
carpeta = "Descargas"
archivos_txt = [archivo for archivo in os.listdir(carpeta) if archivo.endswith('.html')]

for archivo in archivos_txt:
    ruta_archivo = os.path.join(carpeta, archivo)
    if os.path.exists(ruta_archivo):
        try:
            # Abre el archivo en modo lectura ('r')
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo_txt:
                # Lee y muestra el contenido del archivo
                contenido = archivo_txt.read()
                soup = parse_html(contenido)
                tipo_certificado = extraer_destino_residuo(soup)
                if tipo_certificado == "Disposicion Final":
                    tipo_certificado = "Operacion"
                else:
                    tipo_certificado = "Tratamiento"
                fecha = extraer_fecha(soup)
                numero = extraer_numero(soup)
                generador =  extraer_razon_social(soup)
                transportista = extraer_razon_social_transportista(soup)
                operador = extraer_razon_social_destino(soup)
                tipoResiduo = extraer_categoria_y_cantidad(soup)
                kilosResiduo = kilos(soup)
                ids =extraer_cuits(soup)[1]
                cuits=extraer_cuits(soup)[0]
                domicilios= extraer_domicilios(soup)
                localidades= extraer_localidad(soup)
                estado= encontrar_estado(soup)
                
                for i in range(len(tipoResiduo)):
                     insertDB( tipo_certificado,estado, fecha, numero, generador,cuits[0],ids[0],domicilios[0],localidades[0], 
                              transportista,cuits[1],ids[1],domicilios[1],localidades[1],
                               operador,cuits[2],ids[2],domicilios[2],localidades[2], tipoResiduo[i], kilosResiduo[i])
        except IOError:
            print(f"Error al abrir o leer el archivo {ruta_archivo}")     
    
conn.commit()


#c.execute('''SELECT * FROM data''')
sql = pd.read_sql('''SELECT * FROM data''', conn)
#df =pd.DataFrame(sql, columns=columnas)
df = pd.read_sql('''SELECT * FROM data''', conn)

#results = c.fetchall()
#print(results)
conn.close()
#print(df)
numero_archivo = 1
while os.path.exists(f'examples_{numero_archivo}.xlsx'):
    numero_archivo += 1

nombre_archivo = f'examples_{numero_archivo}.xlsx'
nombre_archivo = os.path.join('Excel', f'examples_{numero_archivo}.xlsx')
# Guardar el DataFrame en un archivo Excel

    
df.to_excel(nombre_archivo, index=False)  
print(f"Archivo guardado como {nombre_archivo}")
