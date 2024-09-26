import random
columnas = 6
filas = 6

def lista_random(m,c):
    lst= [0]*(c-m) + [1]*m
    random.shuffle(lst)
    print (lst)
lista_random(2,6)

def asignar_minas(m,f):
    lst=[]
    fila= filas
    for i in range(fila):
        

zero= random.randint(0,3)
print (zero)