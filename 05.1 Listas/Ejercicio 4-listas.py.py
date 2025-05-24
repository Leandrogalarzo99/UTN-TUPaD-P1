# Ejercicio 4 :Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!animales = ["perro", "gato", "conejo", "pez"]


animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"  # Reemplaza el segundo elemento (índice 1)
animales[-1] = "oso"  # Reemplaza el último elemento (índice -1)
print(animales)