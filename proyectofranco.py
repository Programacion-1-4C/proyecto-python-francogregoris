from funciones import *

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
        Adivinar_num()

    if operacion ==2:
        Adivinar_letra()
    if operacion ==3:
        Adivinar_marca()

    if operacion ==4:
        break
       # en caso de que el usuario en el menu toque el numero 4 se termina el programa gracias al break el cual hace que el bucle termine