"""Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función."""



def tabla_multiplicar(numero):
    """
    Imprime la tabla de multiplicar de un número dado del 1 al 10.

    Args:
        numero (int): El número del cual se imprimirá la tabla.
    """
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11): # Rango de 1 a 10 (el 11 es exclusivo)
        print(f"{numero} x {i} = {numero * i}")

# Solicitar el número al usuario
try:
    numero_ingresado = int(input("Introduce un número para ver su tabla de multiplicar: "))

    # Llamar a la función
    tabla_multiplicar(numero_ingresado)

except ValueError:
    print("Entrada inválida. Por favor, introduce un número entero.")