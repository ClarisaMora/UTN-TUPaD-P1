def imprimir_hola_mundo ():
    print("Hola mundo")

def saludar_usuario(_nombre):
    print (f"Te damos la bienvenida a este programa {_nombre}, es un gusto que nos acompañes.")

def informacion_personal(_nombre, _apellido, _edad, _residencia):
    print (f"Soy {_nombre} {_apellido}, tengo {_edad} años y vivo en {_residencia}")

def tabla_multiplicar(_numero):
    for i in range(1, 11):
        resultado = _numero * i
        print(f"{_numero} x {i} = {resultado}")


def operaciones_basicas(_a, _b):
    _suma = _a + _b
    _resta = _a - _b
    _multiplicacion = _a * _b
    # Controlar la división por cero
    if _b != 0:
        _division = _a / _b
    else:
        _division = "Error: división por cero"
    
    return (_suma, _resta, _multiplicacion, _division)
