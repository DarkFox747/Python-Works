def inicio():
    num= int(input('Entre 0 y que numero se encutra tu numero a adivinar?'))
    if num%2 != 0:
        num +=1
    lst=[]
    for i in range(num):
        lst.append(i)
    return lst

def calculo(lst):
    ganaste =""
    lst2=lst
    
    while ganaste !="n":
        a=int(len(lst2)/2)            
        ganaste= input(f'Es {lst[a]} muy alto (a), muy bajo (b), o es tu numero (n)')        
        if ganaste == "a" :
            del lst2[a:]            
        elif ganaste == "b" and a>1:
            del lst2[:a+1]
        if len(lst2) == 1:
            break
    print(f"Tu numero es {lst2[0]}")


def main():
    calculo(inicio())
    while input("Otra pertida? (Y/N): ").upper() == "Y":
        calculo(inicio())

if __name__ == "__main__":
    main()