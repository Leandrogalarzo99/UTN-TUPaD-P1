"""Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario."""



def factorial(n):
    # Caso base: el factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Solicitar al usuario un número
try:
    numero_usuario = int(input("Ingresa un número entero positivo para calcular sus factoriales: "))
    if numero_usuario < 0:
        print("Por favor, ingresa un número entero positivo.")
    else:
        print(f"Calculando factoriales hasta {numero_usuario}:")
        # Calcular y mostrar el factorial de cada número desde 1 hasta el número ingresado
        for i in range(1, numero_usuario + 1):
            print(f"El factorial de {i} es: {factorial(i)}")
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero.")