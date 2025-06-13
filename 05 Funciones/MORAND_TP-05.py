import Funciones_Utiles as FU
#Ejercicio 1: imprimir hola mundo por modulo de funciones
FU.imprimir_hola_mundo()

#Ejercicio 2: Pedir el nombre del usuario y saludarlos mediante modulo de funciones
nombre = input("¿Cuál es tu nombre?: ")
FU.saludar_usuario(nombre)

#Ejercicio 5: Solicitar datos personales y devolverlos por pantalla mediante modulo de funciones
nombre = input ("Ingrese su nombre: ")
apellido = input ("Ingrese su apellido: ")
edad = input ("Ingrese su edad: ")
residencia = input ("Ingrese su domicilio: ")
FU.informacion_personal(nombre, apellido, edad, residencia)

#Ejercicio 6: función que reciba un número como parámetro e imprima la tabla de multiplicar
numero_usuario = int(input("Ingresa un número para ver su tabla de multiplicar: "))
FU.tabla_multiplicar(numero_usuario)

#Ejerciciio 7: dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
resultados = FU.operaciones_basicas (a, b)
print("\nResultados de las operaciones:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")


