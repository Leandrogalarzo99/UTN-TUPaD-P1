"""Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como 
parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados."""




import math # Importamos el módulo math para usar math.pi

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    Args:
        radio (float or int): El radio del círculo.

    Returns:
        float: El área del círculo.
    """
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    """
    Calcula el perímetro de un círculo dado su radio.

    Args:
        radio (float or int): El radio del círculo.

    Returns:
        float: El perímetro del círculo.
    """
    return 2 * math.pi * radio

# Solicitar el radio al usuario
try:
    radio_ingresado = float(input("Introduce el radio del círculo: "))

    # Llamar a las funciones y mostrar los resultados
    area = calcular_area_circulo(radio_ingresado)
    perimetro = calcular_perimetro_circulo(radio_ingresado)

    print(f"El área del círculo es: {area:.2f}") # Formatear a 2 decimales
    print(f"El perímetro del círculo es: {perimetro:.2f}") # Formatear a 2 decimales

except ValueError:
    print("Entrada inválida. Por favor, introduce un número para el radio.")