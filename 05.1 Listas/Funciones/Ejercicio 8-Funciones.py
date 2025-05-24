"""Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales."""



def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC).

    Args:
        peso (float): El peso en kilogramos.
        altura (float): La altura en metros.

    Returns:
        float: El valor del IMC, o None si la altura es cero o negativa.
    """
    if altura <= 0:
        print("Advertencia: La altura debe ser mayor que cero para calcular el IMC.")
        return None
    return peso / (altura ** 2)

# Solicitar los datos al usuario
try:
    peso_ingresado = float(input("Introduce tu peso en kilogramos: "))
    altura_ingresada = float(input("Introduce tu altura en metros: "))

    # Llamar a la función y mostrar el resultado
    imc = calcular_imc(peso_ingresado, altura_ingresada)

    if imc is not None:
        print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")
    else:
        print("No se pudo calcular el IMC debido a datos inválidos.")

except ValueError:
    print("Entrada inválida. Por favor, introduce números para el peso y la altura.")