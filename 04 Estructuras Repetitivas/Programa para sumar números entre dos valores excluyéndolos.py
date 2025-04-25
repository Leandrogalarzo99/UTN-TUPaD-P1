# Ejercicio 3: Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores

valor1 = int(input("Ingrese el primer número entero: "))
valor2 = int(input("Ingrese el segundo número entero: "))

suma = 0
if valor1 < valor2:
    for numero in range(valor1 + 1, valor2):
        suma += numero
elif valor2 < valor1:
    for numero in range(valor2 + 1, valor1):
        suma += numero
else:
    print("Los valores ingresados son iguales, no hay números intermedios.")

if valor1 != valor2:
    print(f"La suma de los números entre {valor1} y {valor2} (excluyéndolos) es: {suma}")