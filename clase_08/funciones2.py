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