import random
def text (lst):
    madlib= f"Si te postran diez veces, te {lst[0]} otras diez, otras cien, otras quinientas: no han de ser tus caídas tan {lst[1]} ni tampoco, por ley, han de ser tantas. Con el hambre genial con que las plantas asimilan el humus avarientas, deglutiendo el rencor de las {lst[2]} se formaron los santos y las santas. Obsesión casi asnal, para ser fuerte, nada más {lst[3]} la criatura, y en cualquier infeliz se me figura que se {lst[4]} los garfios de la suerte... ¡Todos los incurables tienen cura cinco segundos antes de su {lst[5]}!"
    print(madlib)
def Tinicio():
    print("Bienvenido al juego de Madlibs")
    print("El texto es Avanti una poesia de Alma Fuerte")        
def reemplazar():
    lst= ["LEVANTAS","VIOLENTAS","AFRENTAS","NECESITA","MELLAN","MUERTE"]
    lst4= ["LEVANTAS","VIOLENTAS","AFRENTAS","NECESITA","MELLAN","MUERTE"]
    random.shuffle(lst4)
    lst3=["-------","-------","-------","-------","-------","-------",]
    text(lst3)
    print("Tu palabras son: ",lst4)
    a=1
    for i in lst:
             
        palabra=input(f"Cual es la palabra en el lugar {a}? ").upper()
        if palabra==i:
            print("\n")   
            print("Palabra correcta!")          
        else:
            while palabra!=i:
                print("Palabra incorrecta! intenta de nuevo")       
                palabra=input(f"Cual es la palabra en el lugar {a}? ").upper()
        lst3[a-1]=i
        text(lst3)
        lst4.remove(i)
        if len(lst4)<1:
            break
        
        print(f"las palabras restantes son: {lst4}")
        a+=1
    print("GANASTE MASTER!!!")            

def main():
    Tinicio()
    reemplazar()
    while input("Queres jugar de nuevo? (Y/N)").upper() == "Y":
        reemplazar()
        
if __name__ == "__main__":
    main()