"""Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed()."""


def es_palindromo(palabra):
    # Caso base 1: Una cadena vacía o una cadena con un solo carácter es un palíndromo
    if len(palabra) <= 1:
        return True
    # Caso recursivo:
    # Si el primer y último carácter son iguales, se verifica el resto de la cadena
    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1]) # Se llama a la función con la subcadena sin el primer y último carácter
    # Si el primer y último carácter no son iguales, no es un palíndromo
    else:
        return False

# Pruebas de la función
print("Verificador de palíndromos:")
print(f"'reconocer' es un palíndromo: {es_palindromo('reconocer')}") # Esperado: True
print(f"'radar' es un palíndromo: {es_palindromo('radar')}")       # Esperado: True
print(f"'hola' es un palíndromo: {es_palindromo('hola')}")         # Esperado: False
print(f"'ana' es un palíndromo: {es_palindromo('ana')}")           # Esperado: True
print(f"'' (vacío) es un palíndromo: {es_palindromo('')}")         # Esperado: True
print(f"'a' es un palíndromo: {es_palindromo('a')}")               # Esperado: True

# Solicitar al usuario una palabra para verificar
palabra_usuario = input("Ingresa una palabra (sin espacios ni tildes) para verificar si es un palíndromo: ").lower()
if es_palindromo(palabra_usuario):
    print(f"'{palabra_usuario}' SÍ es un palíndromo.")
else:
    print(f"'{palabra_usuario}' NO es un palíndromo.")