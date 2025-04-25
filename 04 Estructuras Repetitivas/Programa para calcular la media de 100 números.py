# Ejercicio 9 : Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor)

cantidad_numeros = 3  # Puedes cambiar esto a 100 para la versión final
suma_total = 0

for i in range(cantidad_numeros):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    suma_total += numero

if cantidad_numeros > 0:
    media = suma_total / cantidad_numeros
    print(f"\nLa media de los {cantidad_numeros} números ingresados es: {media}")
else:
    print("No se ingresaron números para calcular la media.")