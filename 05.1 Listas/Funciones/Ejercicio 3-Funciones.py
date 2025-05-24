"""Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados."""






def informacion_personal(nombre, apellido, edad, residencia):
    """
    Recibe información personal y la imprime en un formato específico.

    Args:
        nombre (str): El nombre de la persona.
        apellido (str): El apellido de la persona.
        edad (int): La edad de la persona.
        residencia (str): La residencia de la persona.
    """
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Solicitar los datos al usuario
nombre_ingresado = input("Introduce tu nombre: ")
apellido_ingresado = input("Introduce tu apellido: ")
edad_ingresada = int(input("Introduce tu edad: ")) # Convertir a entero
residencia_ingresada = input("Introduce tu residencia: ")

# Llamar a la función con los valores ingresados
informacion_personal(nombre_ingresado, apellido_ingresado, edad_ingresada, residencia_ingresada)