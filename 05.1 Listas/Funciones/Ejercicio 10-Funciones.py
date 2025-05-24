"""Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función"""



def calcular_promedio(a, b, c):
    """
    Calcula el promedio de tres números.

    Args:
        a (float or int): El primer número.
        b (float or int): El segundo número.
        c (float or int): El tercer número.

    Returns:
        float: El promedio de los tres números.
    """
    return (a + b + c) / 3

# Solicitar los números al usuario
try:
    num1_prom = float(input("Introduce el primer número: "))
    num2_prom = float(input("Introduce el segundo número: "))
    num3_prom = float(input("Introduce el tercer número: "))

    # Llamar a la función y mostrar el resultado
    promedio = calcular_promedio(num1_prom, num2_prom, num3_prom)
    print(f"El promedio de los tres números es: {promedio:.2f}")

except ValueError:
    print("Entrada inválida. Por favor, introduce números para calcular el promedio.")