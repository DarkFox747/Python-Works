import os
from bs4 import BeautifulSoup
import re
pwd=os.getcwd()

#creador de sopa
def parse_html(html_content):
    return BeautifulSoup(html_content, 'html.parser')
#FUNCION PARA ENCONTRAR EL TIPO DE CERTIFICADO
# Función para extraer la información de destino del residuo
def extraer_destino_residuo(soup):
    # Parsea el contenido HTML con BeautifulSoup
    # Encuentra la sección que contiene "Destino del residuo"
    destino_section = soup.find('p', string='Destino del residuo:')
    # Verifica si se encontró la sección
    if destino_section:
        # Encuentra la siguiente etiqueta <p class="fuente"> que contiene la información deseada
        info_section = destino_section.find_next('p', class_='fuente')
        # Verifica si se encontró la información
        if info_section:
            return info_section.text.strip()  # Devuelve el texto limpio (sin espacios en blanco al inicio y al final)
    
    return "Texto no encontrado"

#FUNCION PARA EXTRAER EL NUMERO Y LA FECHA DEL ARCHIVO
def extraer_numero_fecha(soup):
    # Parsea el contenido HTML con BeautifulSoup
    # Encuentra la sección que contiene el número
    numero_section = soup.find('strong', string=lambda text: "N°" in text)
    numero = numero_section.text.split()[1] if numero_section else "Número no encontrado"
    # Encuentra la sección que contiene la fecha de viaje
    fecha_section = soup.find('strong', string=lambda text: "Fecha de Viaje:" in text)
    fecha = fecha_section.text.split(":")[1].strip() if fecha_section else "Fecha no encontrada"
    
    return fecha,numero

def extraer_numero(soup):
    # Parsea el contenido HTML con BeautifulSoup
    # Encuentra la sección que contiene el número
    numero_section = soup.find('strong', string=lambda text: "N°" in text)
    numero = numero_section.text.split()[1] if numero_section else "Número no encontrado"
    
    return numero

def extraer_fecha(soup):
    # Parsea el contenido HTML con BeautifulSoup
    # Encuentra la sección que contiene la fecha de viaje
    fecha_section = soup.find('strong', string=lambda text: "Fecha de Viaje:" in text)
    fecha = fecha_section.text.split(":")[1].strip() if fecha_section else "Fecha no encontrada"
    return fecha


# Función para extraer la razón social
def extraer_razon_social(soup):
    # Parsea el contenido HTML con BeautifulSoup    
    # Encuentra la sección que contiene la razón social
    razon_social_section = soup.find('p', class_='fuente', string='Razon Social:')
    razon_social = razon_social_section.find_next('p', class_='fuente').text.strip() if razon_social_section else "Razón social no encontrada"
    return razon_social


# Función para extraer la razón social de los transportistas
def extraer_razon_social_transportista(soup):
    # Parsea el contenido HTML con BeautifulSoup   
    # Encuentra la sección que contiene la etiqueta "Transportista"
    transportista_section = soup.find('b', string='Transportista')    
    # Verifica si se encontró la sección del transportista
    if transportista_section:
        # Encuentra la sección que contiene la razón social del transportista
        razon_social_section = transportista_section.find_next('p', class_='fuente', string='Razon Social:')
        razon_social = razon_social_section.find_next('p', class_='fuente').text.strip() if razon_social_section else "Razón social del transportista no encontrada"
    else:
        razon_social = "Sección de transportista no encontrada"    
    return razon_social


# Función para extraer la razón social del destino
def extraer_razon_social_destino(soup):
    # Parsea el contenido HTML con BeautifulSoup
    # Encuentra la etiqueta <b> que contiene el texto "Destino" como marcador
    destino_b = soup.find('b', string='Destino')
    if destino_b:
        # Encuentra la siguiente etiqueta <p class="fuente"> que contiene la razón social del destino
        razon_social_p = destino_b.find_next('p', class_='fuente', string='Razon Social:')
        razon_social = razon_social_p.find_next('p', class_='fuente').text.strip() if razon_social_p else "Razón social del destino no encontrada"
    else:
        razon_social = "Sección de destino no encontrada"
    
    return razon_social


def extraer_categoria_y_cantidad(soup):
    # Parsea el contenido HTML con BeautifulSoup
# Parsea el contenido HTML con BeautifulSoup
    verificacion_residuos_operador = soup.find('p', class_='lead', string='Verificacion Residuos Operador')
    if verificacion_residuos_operador:
        # Encuentra todas las secciones que contienen la información después de la verificación "Residuos Operador"
        secciones = verificacion_residuos_operador.find_all_next('div', class_='row')
        # Lista para almacenar los resultados
        resultados = []
        for seccion in secciones:
            # Busca la sección que contiene la etiqueta <b> con el texto "Categoria Desecho Principal:"
            categoria_desecho = seccion.find('p', class_='fuente', string='Categoria Desecho Principal:')
            if categoria_desecho:
                categoria = categoria_desecho.find_next('p', class_='fuente').text.strip().split()[0]   
                # Busca la cantidad en kilos
                cantidad_kilos = seccion.find('p', class_='fuente', string=lambda text: text and 'Cantidad(Kilos): ' in text)
                cantidad = cantidad_kilos.find_next('p', class_='fuente').text.strip() if cantidad_kilos else "No se encontró la cantidad"
                resultados.append(categoria)
    return resultados


#cantidad de killos: 
def kilos(soup):
# Parsea el contenido HTML con BeautifulSoup    
    verificacion_residuos_operador = soup.find('p', class_='lead', string='Verificacion Residuos Operador')
    if verificacion_residuos_operador:
        # Encuentra todas las secciones que contienen la información después de la verificación "Residuos Operador"
        secciones = verificacion_residuos_operador.find_all_next('div', class_='row')
        # Lista para almacenar los resultados
        resultados = []
        for seccion in secciones:
            # Busca la sección que contiene la etiqueta <b> con el texto "Categoria Desecho Principal:"
            categoria_desecho = seccion.find( string='Cantidad(Kilos): ')
            if categoria_desecho:
                categoria = categoria_desecho.find_next('p', class_='fuente').text.strip().split()[0]
                resultados.append(categoria)
    return resultados

#Encontrar id
def encontrar_id(soup):
    p_id = soup.find('p', string=re.compile(r'Id:\d+'))
    if p_id:
        id_texto = p_id.get_text(strip=True)
        id_numeros = re.search(r'Id:(\d+)', id_texto)
        if id_numeros:
            id_encontrado = id_numeros.group(1)
            return id_encontrado
        else:
            print("No se encontró el ID")
    else:
        print("No se encontró la etiqueta que contiene el ID")


#Encontrar id y cuts para todos
def extraer_cuits(html_content):
    cuits = []
    ids = []
    soup = html_content
    cuit_tags = soup.find_all('p', string=re.compile(r'Id:\d+'))
    for cuit_tag in cuit_tags:
        cuit_text = cuit_tag.get_text(strip=True)
        cuit_number = cuit_text.replace('CUIT:', '').strip().split()[0]
        id_text = cuit_text.replace('CUIT:', '').strip().split()[1]
        id_number = re.search(r'\d+', id_text).group()  # Usar re.search para obtener solo el primer número
        cuits.append(cuit_number)
        ids.append(id_number)
    return cuits, ids

#Funcion para extraer los domicilios
def extraer_domicilios(html_content):
    domicilios = []
    soup = html_content
    domicilio_tags = soup.find_all('p', class_='fuente', string='Domicilio:' )
    for domicilio_tag in domicilio_tags:
        next_div = domicilio_tag.find_next('div', class_='col-auto')
        if next_div:
            domicilio_text = next_div.get_text(strip=True)
            domicilios.append(domicilio_text)
    return domicilios

#Funcion para extraer las localiades
def extraer_localidad(html_content):
    localidades = []
    soup = html_content
    localidad_tags = soup.find_all('p', class_='fuente', string='Localidad:' )
    for localidad_tag in localidad_tags:
        next_div = localidad_tag.find_next('div', class_='col-auto')
        if next_div:
            localidad_text = next_div.get_text(strip=True)
            localidades.append(localidad_text)
    return localidades


#estado de la operacion
def encontrar_estado(html_content):
    soup = html_content
    estado_div = soup.find('div', class_='row alert-info rounded')
    if estado_div:
        col_auto_divs = estado_div.find_all('div', class_='col-auto')
        for col_auto_div in col_auto_divs:
            p_tags = col_auto_div.find_all('p', class_='fuente')
            for p_tag in p_tags:
                if 'ESTADO:' in p_tag.get_text(strip=True):
                    estado_text = col_auto_div.find_next('div', class_='col-auto')
                    if estado_text:
                        estado = estado_text.get_text(strip=True)
                        return estado
    return None

