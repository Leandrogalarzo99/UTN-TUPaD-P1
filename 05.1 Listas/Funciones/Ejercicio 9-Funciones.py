"""Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función."""



def celsius_a_fahrenheit(celsius):
    """
    Convierte una temperatura de grados Celsius a Fahrenheit.

    Args:
        celsius (float or int): La temperatura en grados Celsius.

    Returns:
        float: La temperatura equivalente en Fahrenheit.
    """
    return (celsius * 9/5) + 32

# Solicitar la temperatura en Celsius al usuario
try:
    temp_celsius = float(input("Introduce la temperatura en grados Celsius: "))

    # Llamar a la función y mostrar el resultado
    temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)
    print(f"{temp_celsius}°C equivalen a {temp_fahrenheit:.2f}°F.")

except ValueError:
    print("Entrada inválida. Por favor, introduce un número para la temperatura.")