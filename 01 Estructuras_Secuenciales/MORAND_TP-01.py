print("Hola Mundo")

print("Ejercicio 2")
nombre = input("Ingrese su nombre: ")
print(f"Hola, {nombre}!")

print("Ejercicio 3")
nombreDos = input("Ingrese su nombre: ")
apellido = input(f"Ingrese su apellido {nombreDos}: ")
edad = input(f"Indique su edad {nombreDos}: ")
residencia = input(f"Por último, {nombreDos} ingrese el lugar donde vive: ")
print(f"Soy {nombreDos} {apellido} tengo {edad} años y vivo en {residencia}")

print("Ejercicio 4")
radio = input("Ingrese el radio de circulo: ")
radioNum = float(radio)
pi = 3.14
perimetro = 2 * pi * radioNum
area = pi * radioNum * radioNum
print(f"El perímetro del círculo es: {perimetro}")
print(f"El área del círculo es: {area}")

print("Ejercicio 5")
seg = input ("Ingrese la candidad de segundos: ")
segNum = int(seg)
hora = segNum / 60 / 60
print(f"{seg} segundos equivale a {hora} horas")

print("Ejercicio 6")
numero = int(input("Ingrese un número: "))
print(f"""
{numero} x 0 = {numero * 0}
{numero} x 1 = {numero * 1}
{numero} x 2 = {numero * 2}
{numero} x 3 = {numero * 3}
{numero} x 4 = {numero * 4}
{numero} x 5 = {numero * 5}
{numero} x 6 = {numero * 6}
{numero} x 7 = {numero * 7}
{numero} x 8 = {numero * 8}
{numero} x 9 = {numero * 9}
{numero} x 10 = {numero * 10}
    """)

print("Ejercicio 7")
numUno = int(input("Ingrese un número entero distinto de cero: "))
numDos = int(input("Ingrese otro número entero distinto de cero: "))
numUno != 0
numDos != 0
print (f"""
{numUno} + {numDos} = {numUno + numDos}
{numUno} / {numDos} = {numUno / numDos}
{numUno} x {numDos} = {numUno * numDos}
{numUno} - {numDos} = {numUno - numDos}
   """)

print("Ejercicio 8")
altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso en Kg.: "))
imc = peso / altura ** 2
print (f"Su Indice de Masa Corporal es: {imc}")

print ("Ejercicio 9")
celsius = float(input("Escriba la temperatura: "))
fahren = 1.8 * celsius + 32
print (f"La temperatura {celsius} grados es equivalente a {fahren} grados fahrenheit")

print("Ejercicio 10")
valUno = int(input("Ingrese el primer número: "))
valDos = int(input("Ingrese el segundo número: "))
valTres = int(input("Ingrese el tercer número: "))
promedio = (valUno + valDos + valTres) / 3
print (f"El promedio de los tres valores ingresados es {promedio}")
