"""Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula 𝑛
𝑚 = 𝑛 ∗ 𝑛
(𝑚−1) .Prueba esta función en un algoritmo general."""



def potencia(base, exponente):
    # Caso base: cualquier número elevado a la potencia 0 es 1
    if exponente == 0:
        return 1
    # Caso recursivo: n^m = n * n^(m-1)
    else:
        return base * potencia(base, exponente - 1)

# Prueba la función en un algoritmo general
print("Calculadora de potencia (n^m):")

# Ejemplos de uso
print(f"2 elevado a la 3 es: {potencia(2, 3)}")   # Esperado: 8
print(f"5 elevado a la 0 es: {potencia(5, 0)}")   # Esperado: 1
print(f"10 elevado a la 2 es: {potencia(10, 2)}") # Esperado: 100
print(f"3 elevado a la 4 es: {potencia(3, 4)}")   # Esperado: 81

# Solicitar al usuario valores para probar
try:
    base_usuario = int(input("Ingresa la base (número entero): "))
    exponente_usuario = int(input("Ingresa el exponente (número entero no negativo): "))
    if exponente_usuario < 0:
        print("El exponente debe ser un número entero no negativo.")
    else:
        resultado = potencia(base_usuario, exponente_usuario)
        print(f"{base_usuario} elevado a la {exponente_usuario} es: {resultado}")
except ValueError:
    print("Entrada inválida. Por favor, ingresa números enteros.")