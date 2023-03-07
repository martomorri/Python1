#Guess The Number en Python

import random

def ingresarNivel(msg):
    nivel = int(input(msg))
    while nivel <= 0 or nivel > 3:
        print("\nERROR\n")
        nivel = int(input(msg))
    return nivel

def ingresarNumero1Al1000(msg):
    num = int(input(msg))
    while num < 0 or num > 1000:
        print("\nERROR\n")
        num = int(input(msg))
    return num

print("\n\nBienvenido al Guess The Number\n\n")

nivel = ingresarNivel("\nIngrese un nivel (1 (10 intentos), 2 (5 intentos) o 3 (3 intentos)): ")
r = random.randrange(1,1000)
intentos = 10

if nivel == 2:
    intentos = 5
elif nivel == 3:
    intentos = 3

num = ingresarNumero1Al1000("\nIngrese un numero del 1 al 1000: ")
intentos -= 1

while num != r and intentos > 0:
    print(f"\nUy! Ese no es el numero correcto. Intentelo de nuevo!\nLe quedan {intentos} intentos\n")
    if num > r:
        print("El numero es MENOR al que usted ingreso\n")
    elif num < r:
        print("El numero es MAYOR al que usted ingreso\n")
    num = ingresarNumero1Al1000("\nIngrese un numero del 1 al 1000: ")
    intentos -= 1

if num == r:
    print(f"\nFelicidades! Ganaste!\n")
else:
    print(f"\nPerdiste :( La proxima sera\nEl numero era {r}\n")