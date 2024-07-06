from random import *

numeroAleatorio = randint(1, 100)

intentos = 8
nombre = input("Digita tu nombre: ")

while intentos > 0:
    numero = int(input("Digite el numero: "))
    if numero <= 0:
        print("Tienen que ser numero mayores de 0")
        intentos -= 1
    elif numero > numeroAleatorio:
        print("Te pasaste del numero")
        intentos -= 1
    elif numero < numeroAleatorio:
        print("Tu numero está mas bajo")
        intentos -= 1
    else:
        print("Ganaste")
        print(f"Muy bien {nombre}, te quedaron {intentos} intento(s)")

if intentos == 0:
    print("Mejor suerte la proxima")