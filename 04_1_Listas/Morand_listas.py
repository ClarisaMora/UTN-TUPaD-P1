print("Ejercicio 1")
#lista con los números del 1 al 100 que sean múltiplos de 4
lista1 = list(range(4, 101, 4))
print(lista1)

print("Ejercicio 2")
# Crear una lista con cinco elementos, mostrar el penúltimo
lista2 = [1, 2, "A", "B", True]
lista2_penultimo = lista2 [3] # Con el indexing con números negativos = [-2]
print(lista2_penultimo)

print("Ejercicio 3")
# Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante
lista_vacia = []
lista_vacia.append("Banana")
lista_vacia.append("Pera")
lista_vacia.append("Naranja")
print(lista_vacia)

print("Ejercicio 4")
# Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”
animales = ["perro", "gato", "conejo", "pez"]
print(animales)
animales [1] = "loro"
animales [-1] = "oso"
print(animales)

print("Ejercicio 5")
# Explicar qué hace el siguente código:
numeros = [8, 15, 3, 22, 7]
print (numeros) # Agregamos este print para hacer visible la diferencia en pantalla
numeros.remove(max(numeros)) # La función remueve el número de mayor valor dentro de la lista de números
print (numeros)

print("Ejercicio 6")
# números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros
lista6 = list(range(10, 31, 5))
print(lista6[:2])

print("Ejercicio 7")
#Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera
auto = ["Sedan", "Polo", "Suran", "Gol"]
print(auto)
auto [1] = 15
auto [2] = True
print (auto)

print("Ejercicio 8")
# lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente
dobles = []
dobles.append(5 * 2) #El valor doble de cada número
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

print("Ejercicio 9")
# lista de compras
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo") # a). Agregar "jugo" a la lista del tercer cliente usando append.
print(compras)
compras[1][1] = "tallarines" # b). Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
print (compras)
compras[0].remove("pan") # c). Eliminar "pan" de la lista del primer cliente.
print(compras) #  d). Imprime la lista resultante por pantalla