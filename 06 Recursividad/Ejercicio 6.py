"""Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
 Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión."""


def suma_digitos(n):
    # Caso base: Si el número es 0, la suma de sus dígitos es 0
    if n == 0:
        return 0
    # Caso recursivo:
    # Se suma el último dígito (n % 10) al resultado de la suma de los dígitos del resto del número (n // 10)
    else:
        return (n % 10) + suma_digitos(n // 10)

# Pruebas de la función
print("Calculador de suma de dígitos:")
print(f"La suma de los dígitos de 1234 es: {suma_digitos(1234)}") # Esperado: 10
print(f"La suma de los dígitos de 9 es: {suma_digitos(9)}")       # Esperado: 9
print(f"La suma de los dígitos de 305 es: {suma_digitos(305)}")   # Esperado: 8
print(f"La suma de los dígitos de 7891 es: {suma_digitos(7891)}") # Esperado: 25
print(f"La suma de los dígitos de 0 es: {suma_digitos(0)}")       # Esperado: 0

# Solicitar al usuario un número para calcular la suma de sus dígitos
try:
    numero_usuario = int(input("Ingresa un número entero positivo para sumar sus dígitos: "))
    if numero_usuario < 0:
        print("Por favor, ingresa un número entero positivo.")
    else:
        resultado_suma = suma_digitos(numero_usuario)
        print(f"La suma de los dígitos de {numero_usuario} es: {resultado_suma}")
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero.")