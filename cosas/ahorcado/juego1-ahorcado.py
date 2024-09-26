import random
lista_palabras = ["Universidad", "escuela", "estudiar"]

def getPalabra ():
    palabra= random.choice(lista_palabras)
    return palabra.upper()

def jugar(palabra):        
    plabra_underscore= "_" * len(palabra)
    adivino = False
    vidas = 5
    letras_adivinadas = []
    tuPalabra=[]
    palabra_tick=[]
    print ("Juguemos al ahorcado")
    print (plabra_underscore)
    print ("\n")
    while  not adivino and vidas > 0:
        tuLetra = input("Introduce una letra o palabra").upper()
        if len(tuLetra) == 1 and tuLetra.isalpha():
            if tuLetra in letras_adivinadas:
                print ("ya usaste la letra", tuLetra)
            elif tuLetra not in palabra:
                print ("La letra "+ tuLetra.upper() + " es erronia")
                vidas -=1
                letras_adivinadas.append(tuLetra)
            else:
                print ("La letra "+ tuLetra.upper() + " es correcta")
                letras_adivinadas.append(tuLetra)
        
        elif len(tuLetra) == len(palabra) and tuLetra.isalpha():
            
            