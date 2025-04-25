# Ejercicio 4: ) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0

suma_acumulada = 0
while True:
    numero = int(input("Ingrese un número entero (ingrese 0 para detener): "))
    if numero == 0:
        break
    suma_acumulada += numero
print(f"La suma total de los números ingresados es: {suma_acumulada}")