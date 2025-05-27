"""Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique."""



def fibonacci(posicion):
    # Casos base:
    # El primer término (posición 0 o 1, dependiendo de la convención) es 0
    if posicion == 0:
        return 0
    # El segundo término (posición 1 o 2) es 1
    elif posicion == 1:
        return 1
    # Caso recursivo: F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)

# Solicitar al usuario la posición hasta la cual quiere la serie de Fibonacci
try:
    posicion_limite = int(input("Ingresa la posición hasta la cual quieres ver la serie de Fibonacci: "))
    if posicion_limite < 0:
        print("Por favor, ingresa un número entero no negativo.")
    else:
        print(f"Serie de Fibonacci hasta la posición {posicion_limite}:")
        # Mostrar la serie completa
        for i in range(posicion_limite + 1):
            print(f"F({i}) = {fibonacci(i)}")
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero.")