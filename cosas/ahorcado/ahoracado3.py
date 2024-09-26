import random
lista_palabras = ["Universidad", "escuela", "estudiar","animal"]


def getPalabra ():
    palabra= random.choice(lista_palabras)
    return palabra.upper()

def jugar(palabra):
    tu_palabra=[]
    vidas= 6    
    gano =False
    letras_adivinadas=[]
    plabra_underscore= "_ " * len(palabra)
    print ("Juguemos al ahorcado")
    dibujo(vidas)
    print (plabra_underscore)
    print ("\n")
    while not gano and vidas>0:
        tu_letra = input("Introduce una letra o palabra: ").upper()
        print("\n")
        if len(tu_letra) == 1 and tu_letra.isalpha():
            if tu_letra in letras_adivinadas:
                print ("ya usaste la letra", tu_letra)                
                print("Las letras que usaste son:",letras_adivinadas)
                dibujo(vidas)
            elif tu_letra not in palabra:
                print ("La letra "+ tu_letra + " es erronia")
                vidas =vidas -1 
                letras_adivinadas.append(tu_letra)
                print("Las letras que usaste son:",letras_adivinadas)
                dibujo(vidas)
            else:
                print ("La letra "+ tu_letra.upper() + " es correcta")
                letras_adivinadas.append(tu_letra)
                tu_palabra.append(tu_letra)
                print("Las letras que usaste son:",letras_adivinadas)                
                plabra_underscore=""
                dibujo(vidas)
                for i in palabra:
                    if i in tu_palabra:
                        plabra_underscore+=i
                    else:
                        plabra_underscore+=" _ "
                if len(plabra_underscore) == len(palabra):
                    gano = True
        elif tu_letra == palabra :
            gano = True
            plabra_underscore= tu_letra
            dibujo(vidas)
        elif not tu_letra.isalpha():
            print("Caracter invalido proba de nuevo")
            dibujo(vidas)
        else:
            print ("Derrapaste master, palabra incorreta")
            vidas-=1
            dibujo(vidas)
        
        print(plabra_underscore)
        print("\n")
    if vidas <1:
        print ("Perdiste master! A tomar la chocolatada!")
    else:
        print ("GANASTE KPO SOS GOD")    

def dibujo (vida):
    if vida == 6:
        print(' _____ ')
        print(' |   | ')
        print(' |     ')
        print(' |     ')
        print(' |     ')
        print(' |     ')
        print('---    ')
    elif vida == 5:
        print(' _____ ')
        print(' |   | ')
        print(' |   o ')
        print(' |     ')
        print(' |     ')
        print(' |     ')
        print('---    ')
    elif vida == 4:
        print(' _____ ')
        print(' |   | ')
        print(' |   o ')
        print(' |   | ')
        print(' |     ')
        print(' |     ')
        print('---    ')
    elif vida == 3:
        print(' _____ ')
        print(' |   | ')
        print(' |   o ')
        print(' |   | ')
        print(' |  /  ')
        print(' |     ')
        print('---    ')
    elif vida == 2:
        print(' _____ ')
        print(' |   | ')
        print(' |   o ')
        print(' |   | ')
        print(' |  / \\')
        print(' |     ')
        print('---    ')
    elif vida == 1:
        print(' _____ ')
        print(' |   | ')
        print(' |   o ')
        print(' |  /| ')
        print(' |  / \\')
        print(' |     ')
        print('---    ')
    elif vida == 0:
        print(' _____ ')
        print(' |   | ')
        print(' |   o ')
        print(' |  /|\\')
        print(' |  / \\')
        print(' |     ')
        print('---    ')
        
def main():
    jugar(getPalabra())
    while input("Jugas otro? (Y/N)").upper() == "Y":
        jugar(getPalabra())

if __name__ == "__main__":
    main()