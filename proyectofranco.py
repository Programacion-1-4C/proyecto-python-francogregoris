from random import *
lista_numeros=[n for n in range (1,30)]
intentos=0
elegir=choice(lista_numeros)
listap=[]
# primero lo que hago es importar los datos de la funcion random
contrasenia=123
contra=int(input("ingrese la contrasenia>>>"))
if contra==contrasenia:
    print('contraseña correcta')
elif contra != contrasenia :
      print("contraseña incorrect")
      #le pido al usuario que ponga la contrasenia
while True:
    print(
        "hola buenas este es un juego en el cual tenes que intertar  adivinar la letra, el numero, marca de autos  segun lo que quieras ")
    print('1.adivina el numero ')
    print('2.adivina la letra ')
    print('3. adivina la marca de auto  ')
    print('4.salir')
    # aca escribo un menu y una breve explicacion de lo que hace el juego,
    # despues lo meto en un bucle para que cuando el usuario termine de jugar le aparezca
    operacion = int(input('>>> '))
    if operacion==  1:
        nombre_del_usuario = input("hola! me podrias decir tu nombre? >>> ")
        # esto es simple solo le pregunto al usuario su nombre
        print(f"bueno amigazo/a {nombre_del_usuario} trata de adivinar el numero del 1 al 30 tenes 7 intentos suerte!")
        # aca explico el primer juego el cual trato de adivinar un numero del 1 al 30 en 7 intentos
        while intentos < 7:
            lista_numeros = [n for n in range(1, 30)]
            numero = int(input("ingresa tu numero "))
            intentos += 1
            # en esta parte lo que hago es hacer los intentos diciendo que cada numero que ponga se sume un intento
            if numero < 1:
                print("este numero esta afuera de los parametros puestos ")
            elif numero > 30:
                print("este numero esta afuera de los parametros puestos")
                # lo que hago es que cuando el usuario ingrese un numero mas grande que 30 o mas chico que el 1 le aparezca un cartel de que no esta en los perametrps permitidos
                # esto lo hago usando un if que si el numero puesto es > a 30 le printee el mensaje,y para el 0  hago lo contrario
            elif numero > elegir:
                print("el numero a encontrar  es mas chico ")
            elif numero < elegir:
                print("el numero a encontrar es mas grande ")
                # aca lo que hago es para que el progama no sea tan dificil darle ayudas al usuario avisandole que el numero a encontrar es mas grande o chico al cual el printeo
            elif numero == elegir:
                print("felicidades le pegaste al numero!!")
                print(f"la cantidad de intentos que te tomo fue {intentos}")
                break
                #por ultimo de la primera parte si el numero ingresado por el usuario es igual al generado le salga un cartel de efelicitaciones al usuario
                #despues poner un contador de los intentos del usuario para adivinar el numero y al final generar un break
            elif numero == 7:
                print("no pudiste adivinar el numero ")
                print(f"el numero era{elegir} ")
                # aca priteo que el usuario no adivino el numero y cual era
    if operacion ==2:
        lista_letras = ["a", "b", "c", "d", "e,"f",g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "u"]
        intentos = 0
        # creo la lista con las letras a usar y pongo la cantidad de intentos los cuales inicia el usuario
        elegir = choice(lista_letras)
        nombre_del_usuario = input("hola! me podrias decir tu nombre? >>> ")
        print(
            f"bueno amigazo/a {nombre_del_usuario} trata de adivinar una  letra entre la A y la U tenes 10 intentos suerte!")
        while intentos < 10:
            letra = input("ingresa tu letra >>>")
            intentos += 1
            if len(letra) != 1:
                print("escribe una sola letra ")
            elif letra == elegir:
                print("felicidades le pegaste a la letra!!")
                print(f"la cantidad de intentos que te tomo fue {intentos}")
                break
            elif letra == 10:
                print("no pudiste adivinar la letra ")
                print(f"la letra era{elegir} ")
                #repito el mismo proceso que con los numeros  nada mas que aca uso un len para que el usuario no pueda gregar mas de una letra ej;aa
    if operacion ==3:
        lista_autos =["renault",'fiat',"volkswagen","mclaren","ford",'chevrolet',"ferrari","mercedes","honda","nissan","bugatti",'toyota']
        intentos = 0
        elegir = choice(lista_autos)
        nombre_del_usuario = input("hola! me podrias decir tu nombre? >>> ")
        print(
        f"bueno amigazo/a {nombre_del_usuario} trata de adivinar entre estas marcas:renault,fiat,volkswagen,mclaren,ford,chevrolet,ferrari,mercedes,honda,nissan,bugatti !")
        while intentos < 10:
            intentos += 1
            marca_de_autos = input("ingresa tu marca de auto >>>")
            if marca_de_autos in listap:
                print('valor ya usado')
            else:
                listap.append(marca_de_autos)
            print(f"{intentos}")
            if marca_de_autos == elegir:
               print("felicidades adivanste!!")
               print(f"la cantidad de intentos que te tomo fue {intentos}")
    if operacion ==4:
        break
       # en caso de que el usuario en el menu toque el numero 4 se termina el programa gracias al break el cual hace que el bucle termine
