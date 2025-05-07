print ("Ejercicio 1")
#Solicite la edad del usuario. Si el usuario es mayor de 18 años: en pantalla que diga “Es mayor de edad”.
edad = int (input ("Por favor ingrese su edad: "))
if edad >= 18 :
    print ("Es mayor de edad")
else:
    pass

print("Ejercicio 2")
#Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
nota = int (input ("Por favor ingrese su calificación: "))
if nota >= 6 :
    print ("Aprobado")
else:
    print ("Desaprobado")

print("Ejercicio 3")
#Ingresar solo números pares. Si el número es par "Ha ingresado un número par"; si no "Por favor, ingrese un número par".
numero_par = int (input ("Por favor ingrese un número par: "))
if numero_par % 2 == 0 :
    print ("Ha ingresado un número par")
else:
    print ("Por favor, ingrese un número par")

print ("Ejercicio 4")
#Solicitar edad e imprimoir por pantalla a qué categorías pertenece (niño, adolescente, adulto joven, adulto)
edad = int (input ("Por favor ingrese su edad: "))
if edad < 12 :
    print ("Categoría: NIÑO")
elif edad >= 12 and edad < 18 :
    print ("Categoría: ADOLESCENTE")
elif edad >= 18 and edad < 30 :
    print ("Categoría: ADULTO JÓVEN")
else:
    print ("Categoría: ADULTO")

print ("Ejercicio 5")
#Escribir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14)
contra = input ("Escriba una contraseña que contenga ente 8 y 14 caracteres: ")
contra_cantidad = len (contra)
if contra_cantidad < 8 or contra_cantidad > 14 :
    print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
else :
    print ("Ha ingresado una contraseña correcta")

print ("Ejercicio 6")
#Tomar lista de numeros aleatorios: calcular moda(mode), mediana(median) y media(mean). Determinar sesgo positivo, negativo o no hay sesgo
from statistics import mode, median, mean
import random
num_aleatorios = [random.randint(1, 100) for i in range (20)]
moda = mode (num_aleatorios)
mediana = median (num_aleatorios)
media = mean (num_aleatorios)

print (f"Secuencia de números: {num_aleatorios}")
print (f"Moda: {moda}, Mediana: {mediana}, Media: {media}")

if (media > mediana) and (mediana > moda) :
    print("Sesgo positivo")
elif (media < mediana) and (mediana < moda):
    print ("Sesgo negativo")
elif media == mediana == moda :
    print ("Sin sesgo")
else :
    print ("No se puede definir el sesgo")

print ("Ejercicio 7")
#Solicitar frase o palabra. Si ternina en vocal, añadir un signo de exclamación al final
frase = input ("Escribe aun frase o palabra: ")
ultima_letra = frase [- 1].lower()
print (ultima_letra)
if (ultima_letra == "a") or (ultima_letra == "e") or (ultima_letra == "i") or (ultima_letra == "o") or (ultima_letra == "u") :
    print (f"{frase}!!")
else :
    print (frase)

print ("Ejercicio 8")
#Convertir el input: todo a mayuscula, todo a minuscula, la primer letra en mayuscula según se seleccione 1, 2 o 3
nombre = input("Hola! Por favor ingresa tu nombre: ")
print ("Podemos mostrarte tu nombre de 3 formas:")
print ("1. Todo en mayúsculas")
print ("2. Todo en minúsculas")
print ("3. La primera letra en mayuscula")
modo = input("Como te gustaría visualizar tu nombre?. Ingresa el número que corresponde: ")
if modo == "1" :
    print (nombre.upper())
elif modo == "2" :
    print (nombre.lower())
elif modo == "3" :
    print (nombre.title())
else :
    print ("El valor ingresado no es correcto. Por favor ingrese 1, 2 o 3")

print ("Ejercicio 9")
#Pedir magnitudes de un terremoto en escala Richter y y clasificar
magnitud = float (input("Escriba la magnitud del terremoto: "))
if magnitud < 3 :
    print ("Muy leve (imperceptible)")
elif magnitud >=3 and magnitud < 4: 
    print ("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5 : 
    print ("Moderado (sentido por personas pero generalmente no causa daño)")
elif magnitud >= 5 and magnitud < 6 :
    print ("Fuerte (puede caudar daño en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7 :
    print ("Muy fuerte (puede causar daños significativos)")
elif magnitud >= 7 :
    print ("Extremo (puede causar graves daños a gran escala)")
else :
    pass