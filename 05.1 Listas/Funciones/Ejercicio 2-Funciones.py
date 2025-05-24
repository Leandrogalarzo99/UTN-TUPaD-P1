"""Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario."""

def saludar_usuario(nombre):
    """
    Recibe un nombre como parámetro y devuelve un saludo personalizado.

    Args:
        nombre (str): El nombre del usuario.

    Returns:
        str: Un saludo personalizado.
    """
    return f"Hola {nombre}!"

# Solicitar el nombre al usuario
nombre_usuario = input("Por favor, introduce tu nombre: ")

# Llamar a la función y mostrar el resultado
saludo = saludar_usuario(nombre_usuario)
print(saludo)