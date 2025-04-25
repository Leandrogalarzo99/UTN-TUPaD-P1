# Ejercicio 6 : Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros

numeros_saltos = list(range(10, 31, 5))
dos_primeros = numeros_saltos[:2]
print(dos_primeros)