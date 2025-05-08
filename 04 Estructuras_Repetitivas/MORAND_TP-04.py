print ("Ejercicio 1")
#Todos los números enteros de 0 a 100 (ambos extremos), en orden creciente, mostrando un número por línea
for numero in range (0, 101):
    print(numero)

print ("Ejercicio 2")
#Solicite al usuario un número entero y determine la cantidad de dígitos que contiene
entero = input("Escriba un número entero (sin comas): ")
if "," in entero or "." in entero: #nos aseguramos que el número (que es un str) no tenga puntos o comas
    print ("Entrada no válida, el número debe ser un entero")
else:
    entero_pos = entero.lstrip("-") #omitimos el signo negativo si lo tuviese
    cant_entero = len (entero_pos)
    print (f"Su número contiene {cant_entero} dígitos.")

print("Ejercicio 3")
# Sumar números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores
num1 = int (input("Ingrese un número entero: "))
num2 = int (input ("Ingrese otro número entero: "))
primero = min (num1, num2)
ultimo = max (num1, num2)
suma = 0
for valores in range(primero + 1, ultimo):
    suma += valores #Que es como decir: suma = suma + valores
print (f"La suma del rango de valores es {suma}")

print ("Ejercicio 4")
#Ingresar números enteros que se sumen en secuencia. Input = 0 El programa debe detenerse y mostrar el total
sumatoria = 0
print("Ingresa números enteros para sumarlos. Escribe 0 para finalizar.")
while True:
    numero = int(input("Ingresa un número: "))
    if numero == 0:
        break
    sumatoria = sumatoria + numero
print (sumatoria)

print ("Ejercicio 5")
import random
num_secreto = random.randint(0, 9)
intentos = 0
print("Adivina el número entre 0 y 9.")
while True:
    intento = int(input("Qué número podría ser?: "))
    intentos += 1
    if intento == num_secreto:
        print(f"Adivinaste! El número era {num_secreto}.")
        print(f"Fueron necesarios {intentos} intento/s para conseguirlo")
        break
    else:
        print("Incorrecto. Intenta de nuevo.")

print ("Ejercicio 6")
#números pares comprendidos entre 0 y 100, en orden decreciente
for numero in range (100, -1, -2):
    print(numero)

print ("Ejercicio 7")
#Suma de números entre 0 y un número entero positivo indicado por el usuario 
suma_total = 0
numero_usuario = int( input("Ingrese un número entero positivo: ") ) #Le damos la condición de entero con int()
if numero_usuario < 0: #Nos aseguramos de que el número sea positivo
    print("Ingrese un valor mayor que cero")
else:  
    for numero in range (0, numero_usuario +1): #+1 para que incluya el valor ingresado por el usuario en la suma
        suma_total += numero
    print(f"La suma de 0 a {numero_usuario} es {suma_total}")