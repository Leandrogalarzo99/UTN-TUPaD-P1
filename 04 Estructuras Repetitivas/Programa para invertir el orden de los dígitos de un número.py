# Ejercicio 10 : Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745

numero_str = input("Ingrese un número entero: ")
numero_invertido_str = numero_str[::-1]
print(f"El número invertido es: {numero_invertido_str}")