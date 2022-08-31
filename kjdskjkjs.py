from random import *
lista_letras=[n for n in range ("a","b","c","d","e,"f",g","h","i","j","k","l","m","n","o","p","q","r","s","u","v","w",'y',"z")]
intentos=0
elegir=choice(lista_letras)
nombre_del_usuario=input("hola! me podrias decir tu nombre? >>> ")
print(f"bueno amigazo/a {nombre_del_usuario} trata de adivinar la letra entre la A y la Z tenes 10 intentos suerte!")
while intentos<7:
    letra=int(input("ingresa tu letra "))
    intentos+=1
    if letra<1:
        print("esta letra esta afuera de los parametros puestos ")
    elif letra>30:
        print("esta letra esta afuera de los parametros puestos")
    elif letra>elegir:
        print("la lta encontrar  es mas chico ")
    elif letra<elegir:
        print("la letra a encontrar es mas grande ")
    elif letra==elegir:
        print("felicidades le pegaste a la letra!!")
        print(f"la cantidad de intentos que te tomo fue {intentos}")
        break
    elif letra==7:
        print("no pudiste adivinar la letra ")
        print(f"la letra era{elegir} ")