"""Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número,"""



def contar_digito(numero, digito):
    # Caso base: Si el número es 0, el dígito ya no puede aparecer, por lo que la cuenta es 0.
    # Excepción: si el número original es 0 y el dígito buscado es 0, debe retornar 1.
    if numero == 0:
        return 1 if digito == 0 else 0
        
    # Si el número se convierte en 0 después de la división, ya no hay más dígitos
    if numero < 10 and numero != 0:
        return 1 if numero == digito else 0
    elif numero == 0 and digito == 0:
        return 1
    elif numero == 0:
        return 0


    # Inicializa el contador para este nivel de recursión
    apariciones = 0

    # Comprueba si el último dígito del número es igual al dígito buscado
    if (numero % 10) == digito:
        apariciones = 1

    # Llamada recursiva con el resto del número (sin el último dígito)
    return apariciones + contar_digito(numero // 10, digito)

# Pruebas de la función
print("Contador de dígitos:")
print(f"El dígito 2 aparece {contar_digito(12233421, 2)} veces en 12233421") # Esperado: 3
print(f"El dígito 5 aparece {contar_digito(5555, 5)} veces en 5555")         # Esperado: 4
print(f"El dígito 7 aparece {contar_digito(123456, 7)} veces en 123456")     # Esperado: 0
print(f"El dígito 0 aparece {contar_digito(10020, 0)} veces en 10020")       # Esperado: 3
print(f"El dígito 0 aparece {contar_digito(0, 0)} veces en 0")               # Esperado: 1
print(f"El dígito 1 aparece {contar_digito(1, 1)} veces en 1")               # Esperado: 1
print(f"El dígito 2 aparece {contar_digito(1, 2)} veces en 1")               # Esperado: 0


# Solicitar al usuario un número y un dígito
try:
    num_usuario = int(input("Ingresa un número entero positivo: "))
    dig_usuario = int(input("Ingresa el dígito a buscar (0-9): "))

    if num_usuario < 0:
        print("Por favor, ingresa un número entero positivo.")
    elif not (0 <= dig_usuario <= 9):
        print("Por favor, ingresa un dígito entre 0 y 9.")
    else:
        conteo = contar_digito(num_usuario, dig_usuario)
        print(f"El dígito {dig_usuario} aparece {conteo} veces en el número {num_usuario}.")
except ValueError:
    print("Entrada inválida. Por favor, ingresa números enteros.")