import time
nombre = input("¿Comó te llamas?")
print("Hola, "+nombre," Es hora de jugar al ahorcado")
print(" ")
time.sleep(1)
print("Comienza a adivinar")
time.sleep(0.5)
palabra='cctmexico'
tupalabra=''
vidas=5

while vidas>0:
    fallas=0
    for letra in palabra:
        if letra in tupalabra:
            print(letra, end="")
        else:
            print("*",end="")
            fallas+=1
    if fallas==0:
        print("Felicidades, ganaste")
        break

    tuletra=input("Introduce una letra: ")
    tupalabra+=tuletra

    if tuletra not in palabra:
        vidas-=1
        print("Equivocación")
        print("Tu tienes ",+vidas," Vidas")
    if vidas == 0:
        print("Perdiste")
else:
    print("Gracias por participar") 
