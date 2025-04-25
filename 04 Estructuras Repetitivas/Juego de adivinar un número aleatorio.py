# Ejercicio 5: Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número

import random

numero_secreto = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1
    if intento == numero_secreto:
        print(f"¡Felicitaciones! Adivinaste el número en {intentos} intentos.")
        break
    elif intento < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")