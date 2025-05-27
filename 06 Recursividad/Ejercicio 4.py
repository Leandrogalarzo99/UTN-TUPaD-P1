"""Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.
Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
procedimiento:
1. Dividir el número por 2.
2. Guardar el resto (0 o 1).
3. Repetir el proceso con el cociente hasta que llegue a 0.
4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario."""



def decimal_a_binario(numero_decimal):
    # Caso base: si el número es 0, su representación binaria es "0"
    if numero_decimal == 0:
        return "0"
    # Caso recursivo:
    # Si el número es 1, su representación binaria es "1"
    elif numero_decimal == 1:
        return "1"
    # Para otros números, dividimos por 2 y agregamos el resto al resultado de la recursión
    else:
        # Calcular el resto (0 o 1)
        resto = numero_decimal % 2
        # Calcular el cociente para la próxima llamada recursiva
        cociente = numero_decimal // 2
        # La representación binaria es la del cociente más el resto actual
        return decimal_a_binario(cociente) + str(resto)

# Prueba la función
print("Convertidor de decimal a binario:")

# Ejemplos:
print(f"El número 10 en binario es: {decimal_a_binario(10)}") # Esperado: 1010
print(f"El número 25 en binario es: {decimal_a_binario(25)}") # Esperado: 11001
print(f"El número 1 en binario es: {decimal_a_binario(1)}")   # Esperado: 1
print(f"El número 0 en binario es: {decimal_a_binario(0)}")   # Esperado: 0

# Solicitar al usuario un número para convertir
try:
    num_usuario = int(input("Ingresa un número entero positivo para convertir a binario: "))
    if num_usuario < 0:
        print("Por favor, ingresa un número entero positivo.")
    else:
        resultado_binario = decimal_a_binario(num_usuario)
        print(f"El número {num_usuario} en binario es: {resultado_binario}")
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero.")