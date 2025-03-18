

import random


numero_secreto = random.randint(0,101)
cant_intentos = 0
cant_max_intentos = 5
adivinado = False


print("¡Bienvenidos al juego de adivinar el numero!")

while not adivinado:
    if not cant_intentos < cant_max_intentos:
        print("Game over, no haz podido adivinar el numero")
        break


    entrada = input("Introduce un numero del 1 al 99 ")#TODO
    numero = int(entrada)

    if numero == numero_secreto:
        print("¡Felicidades has adivinado!")
        adivinado = True
    elif numero < numero_secreto:
        print("El numero es mayor al ingresado")
    else:
        print("El numero es menor al ingresado")
    
    cant_intentos += 1