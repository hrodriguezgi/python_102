"""
Vamos a crear tres funciones simples
las cuales serán llamadas desde otra 
función: operaciones
"""

def sumar(valor_1, valor_2):
    return valor_1 + valor_2

def restar(valor_1, valor_2):
    return valor_1 - valor_2

def multiplicar(valor_1, valor_2):
    return valor_1 * valor_2

def operaciones(valor_1=10, valor_2=20):
    return sumar(valor_1, valor_2), restar(valor_1, valor_2), multiplicar(valor_1, valor_2)

print()
print(operaciones(3, 4))

print(operaciones(1))

print(operaciones())
print()


"""
Algunos casos de uso de las funciones 
y los parámetros.
"""

print(restar(10, 2))
print(restar(2, 10))

print()
suma = sumar(3, 4)
print(f'El resultado de la suma es: {suma}')
print()

"""
Algunos casos de uso del return
"""

resultado = operaciones(5, 8)
print(f'El resultado de las operaciones es {resultado}')
print(f'El resultado de la suma es {resultado[0]}')
print(f'El resultado de la resta es {resultado[1]}')
print(f'El resultado de la multiplicacion es {resultado[2]}')
print()

r_sum, r_res, r_mul = operaciones(9, 3)
print(f'El resultado de la suma es {r_sum}')
print(f'El resultado de la resta es {r_res}')
print(f'El resultado de la multiplicacion es {r_mul}')
print()

r_suma, *r_otras = operaciones(12, 43)
print(f'El resultado de la suma es {r_suma}')
print(f'El resultado de la resta es {r_otras[0]}')
print(f'El resultado de la multiplicacion es {r_otras[1]}')
print()

"""
Parámetros variables
"""
# Posición variable
def sumar_v2(valor_1, valor_2, *valores):
    print(type(valores), valores)
    suma = 0
    for valor in valores:
        suma += valor
    return valor_1 + valor_2 + suma

print(sumar_v2(1,2))
print()
print(sumar_v2(1,2,3,4,5,6))
print()

def sumar_v3(valor_1, valor_2, *args):
    suma = sum(args)
    return valor_1 + valor_2 + suma

print(f'El resultado de la suma es: {sumar_v3(1,2)}')
print()
print(f'El resultado de la suma es: {sumar_v3(1,2,3,4,5,6)}')
print()


def sumar_v4(valor_1, valor_2=10, *args):
    suma = sum(args)
    return valor_1 + valor_2 + suma

print(f'El resultado de la suma_v4 es: {sumar_v4(2)}')
print()
print(f'El resultado de la suma_v4 es: {sumar_v4(3,12)}')
print()
print(f'El resultado de la suma_v4 es: {sumar_v4(1,2,3,4,5,6)}')
print()

# llave-valor variable
import json

def crear_estudiante(nombre, apellido, activo, **datos):
    estudiante = dict()
    estudiante['nombre'] = nombre
    estudiante['apellido'] = apellido
    estudiante['activo'] = activo
    #print(type(datos), datos)
    estudiante.update(datos)
    return json.dumps(estudiante)

print(crear_estudiante('Andres', 'Toro', False))
print()
print(crear_estudiante('Carlos', 'Aguirre', False, edad=10, sexo='Masculino', grado='quinto'))
print()
print(crear_estudiante('Eduard', 'Hoyos', False, edad=12, grado='septimo'))
print()

# Función con *args y **kwargs
def completa(val_1, val_2, val_3=10, *vals, **kwvals):
    mul = val_1 * val_2 * val_3
    suma = sum(vals)
    dicc = { key: value for key, value in kwvals.items() }
    return mul, suma, dicc

print(completa(10, 2, 4, 5, 6, nombre='Harvey', apellido='Rodriguez'))
print(completa(30, 4))
print()


# Recursividad
# factorial de un número es la multiplicación de todos sus antecesores
# 5! = 5 x 4 x 3 x 2 x 1
# 1! = 1

def factorial(x):
    print(x)
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)
    
#print(factorial(1))
print(factorial(5))
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1
print()

# Funciones de Mayor Jerarquía o Mayor Orden
def saludo():
    print('hola')

saludo()

lista = [1,2,3,4,5]

def cuadrado(num):
    return num ** 2

lista_2 = list(map(cuadrado, lista))
print(lista_2)
print()

def operaciones_v2(num_1, num_2, operacion):
    return operacion(num_1, num_2)

print(operaciones_v2(3, 5, sumar))