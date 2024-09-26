import time;
nombre=input("Ingresa tu nombre.");
print("Hola, "+nombre,"Juguemos al ahorcado!");
print(" ");
time.sleep(1);
print ("Comienza a adivinar (ingresa letras minúsculas)");
time.sleep(0.5);
palabra='universidad';
tupalabra='';
vidas=5;

while vidas > 0:
    fallas=0;
    for letra in palabra:
        if letra in tupalabra:
            print(letra, end="")
        else:
            print ("_", end="")
            fallas+=1;
    if fallas==0:
        print ("Felicidades, haz ganado!")
        break
    print ("")
    tuletra=input("introduce una letra: ")
    tupalabra+=tuletra

    if tuletra not in palabra:
        vidas-=1
        print("ERROR!")
        print("Te quedan ", +vidas, " vidas")
        if vidas == 0:
         print ("HAZ PERDIDO!")
else:
    print ("Gracias por jugar!")
    