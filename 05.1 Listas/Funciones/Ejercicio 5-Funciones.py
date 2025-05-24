"""Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función"""



def segundos_a_horas(segundos):
    """
    Convierte una cantidad de segundos a horas.

    Args:
        segundos (int or float): La cantidad de segundos.

    Returns:
        float: La cantidad de horas.
    """
    return segundos / 3600 # Hay 3600 segundos en una hora

# Solicitar los segundos al usuario
try:
    segundos_ingresados = float(input("Introduce la cantidad de segundos: "))

    # Llamar a la función y mostrar el resultado
    horas = segundos_a_horas(segundos_ingresados)
    print(f"{segundos_ingresados} segundos equivalen a {horas:.4f} horas.") # Formatear a 4 decimales

except ValueError:
    print("Entrada inválida. Por favor, introduce un número para los segundos.")