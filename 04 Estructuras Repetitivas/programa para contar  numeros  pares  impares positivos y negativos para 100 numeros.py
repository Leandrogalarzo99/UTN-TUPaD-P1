# Ejercicio 8 :Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio)

cantidad_numeros = 3  # Puedes cambiar esto a 100 para la versión final
pares = 0
impares = 0
positivos = 0
negativos = 0

for _ in range(cantidad_numeros):
    numero = int(input("Ingrese un número entero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"\nDe los {cantidad_numeros} números ingresados:")
print(f"  - Pares: {pares}")
print(f"  - Impares: {impares}")
print(f"  - Positivos: {positivos}")
print(f"  - Negativos: {negativos}")