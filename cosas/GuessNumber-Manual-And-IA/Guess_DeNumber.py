import random

def generate_random(x):
    a= random.randint(0,x)
    return a

def dificultad():
    dif= ""
    dificultades=["FACIL","INTERMEDIO","DIFICIL"]
    while dif not in dificultades:
        dif= input('Dificultades: \n de 0 a 10 = FACIL \n de 0 a 20 =INTERMEDIO \n de 0 a 50 = DIFICL \n Seleccion la dificultad: ').upper()
    if dif== "FACIL":
        return 10
    elif dif== "INTERMEDIO":
        return 20
    elif dif== "DIFICIL":
        return 50

def guess(random,b):
    num = int(input(f"Hora de adivinar! Selecciiona un numero entre 0 y {b}: "))
    while num != random:
        if num < random:
            num= int(input("Error! Tu numero fue muy bajo, intenta de nuevo: "))
        elif num > random:
            num= int(input("Error! Tu numero fue muy alto, intenta de nuevo: "))
    print (f"LO CONESEGUISTE!! Adivinaste el numero {num}")

def main():
    a= dificultad()
    guess(generate_random(a),a)
    while input("Queres jugar de nuevo? Y/N: ").upper() == "Y":
        b=dificultad()
        guess(generate_random(b),b)
        
if __name__ == "__main__":
    main()