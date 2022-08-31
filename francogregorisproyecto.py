from random import *
lista_numeros=[n for n in range (1,30)]
intentos=0
elegir=choice(lista_numeros)
nombre_del_usuario=input("hola! me podrias decir tu nombre? >>> ")
print(f"bueno amigazo/a {nombre_del_usuario} trata de adivinar el numero del 1 al 30 tenes 7 intentos suerte!")
while intentos<7:
    numero=int(input("ingresa tu numero "))
    intentos+=1
    if numero<1:
        print("este numero esta afuera de los parametros puestos ")
    elif numero>30:
        print("este numero esta afuera de los parametros puestos")
    elif numero>elegir:
        print("el numero a encontrar  es mas chico ")
    elif numero<elegir:
        print("el numero a encontrar es mas grande ")
    elif numero==elegir:
        print("felicidades le pegaste al numero!!")
        print(f"la cantidad de intentos que te tomo fue {intentos}")
        break
    elif numero==7:
        print("no pudiste adivinar el numero ")
        print(f"el numero era{elegir} ")