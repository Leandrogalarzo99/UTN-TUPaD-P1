# Ejercicio 7 : Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario


limite = int(input("Ingrese un número entero positivo: "))
suma = 0
for numero in range(limite + 1):
    suma += numero
print(f"La suma de los números desde 0 hasta {limite} es: {suma}")