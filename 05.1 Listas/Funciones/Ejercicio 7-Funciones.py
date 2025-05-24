"""Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara."""



def operaciones_basicas(a, b):
    """
    Realiza suma, resta, multiplicación y división de dos números.

    Args:
        a (float or int): El primer número.
        b (float or int): El segundo número.

    Returns:
        tuple: Una tupla que contiene (suma, resta, multiplicacion, division).
               La división es None si b es 0.
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = None # Inicializamos la división como None

    if b != 0:
        division = a / b
    else:
        print("Advertencia: No se puede dividir por cero.")

    return (suma, resta, multiplicacion, division)

# Solicitar los números al usuario
try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    # Llamar a la función y mostrar los resultados
    resultados = operaciones_basicas(num1, num2)

    print(f"Suma: {resultados[0]}")
    print(f"Resta: {resultados[1]}")
    print(f"Multiplicación: {resultados[2]}")
    if resultados[3] is not None:
        print(f"División: {resultados[3]:.2f}") # Formatear a 2 decimales
    else:
        print("División: Indefinida (división por cero)")

except ValueError:
    print("Entrada inválida. Por favor, introduce números.")