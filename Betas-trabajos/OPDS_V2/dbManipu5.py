import sqlite3

conn = sqlite3.connect('localDB')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS data(
    Tipo_certificado TEXT, 
    Estado TEXT, 
    Fecha DATE, 
    Manifiesto INTEGER PRIMARY KEY, 
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
    kilos_Residuo INTEGER
)''')

def manifiesto_existente(manifiesto):
    c.execute("SELECT 1 FROM data WHERE Manifiesto = ?", (manifiesto,))
    return c.fetchone() is not None

def insertDB(tipo_certificado, estado, fecha, numero, generador, Cuit_Generador, ID_Generador, Domicilio_Generador, Localidad_Generador, 
             transportista, Cuit_Transportista, ID_Transportista, Domicilio_Transportista, Localidad_Transportista,
             operador, Cuit_Operador, ID_Operador, Domicilio_Operador, Localidad_Operador,
             tipoResiduo, kilosResiduo):
    if not manifiesto_existente(numero):
        c.execute('''INSERT INTO data VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', 
                  (tipo_certificado, estado, fecha, numero, generador, Cuit_Generador, ID_Generador, Domicilio_Generador, Localidad_Generador, 
                   transportista, Cuit_Transportista, ID_Transportista, Domicilio_Transportista, Localidad_Transportista,
                   operador, Cuit_Operador, ID_Operador, Domicilio_Operador, Localidad_Operador, tipoResiduo, kilosResiduo))
