# Funciones

print(f"{10*'*'} Función 'print()' {10*'*'}\n")

print('Ejemplo 1:\n')
print(f'print("Hola Mundo")')
print("Hola Mundo\n\n")

print('Ejemplo 2:\n')
str1 = 'Hola Mundo'
str2 = 'Cruel'
print(f"print(str1, str2, sep='*-*', end='')")
print(str1, str2, sep='*-*', end='')



print('\n\n\n')
print(f"{10*'*'} Función 'isinstance()' {10*'*'}\n")

print('Ejemplo 1:\n')
numeros = [1,2,3,4]
print('print(isinstance(numeros, list))')
print(isinstance(numeros, list),'\n')

print('Ejemplo 2:\n')
print('isinstance(numeros, dict)')
print(isinstance(numeros, dict))



print('\n\n\n')
print(f"{10*'*'} Función 'zip()' {10*'*'}\n")

print('Ejemplo 1:\n')
numeros = [1, 2, 3, 4, 5]
vocales = ['a', 'e', 'i', 'o', 'u']
print('print(zip(numeros, vocales))')
print(zip(numeros, vocales))
print('\nprint(list(zip(numeros, vocales)))')
print(list(zip(numeros, vocales)),'\n')

print('Ejemplo 2:\n')
print('numeros.append(6)')
numeros.append(6)
print(f'numeros: {numeros}')
print(f'print(list(zip(numeros, vocales))')
print(list(zip(numeros, vocales)),'\n')

print('Ejemplo 3:\n')
secuencia = [(1,'a','a'), (2,'e','v'), (3,'i','i'), (4,'o','o'), (5,'u','n')]
print(f'secuencia: {secuencia}')
print('num, voc, pal = zip(*secuencia)')
num, voc, pal = zip(*secuencia)
print('num:', num)
print('voc:', voc)
print('pal:', pal)



print('\n\n\n')
print(f"{10*'*'} Función 'map()' {10*'*'}\n")

print('Ejemplo 1:\n')
vocales = ['a', 'e', 'i', 'o', 'u']
print(f'vocales: {vocales}')
print('VOCALES = list(map(str.upper, vocales))')
VOCALES = list(map(str.upper, vocales))
print(VOCALES,'\n')

print('Ejemplo 2:\n')
from math import sqrt
numeros = [1, 4, 9, 16, 25]
print(numeros)
print('raices = list(map(sqrt, numeros))')
raices = list(map(sqrt, numeros))
print(raices)



print('\n\n\n')
print(f"{10*'*'} Función 'filter()' {10*'*'}\n")

print('Ejemplo 1:\n')
numeros = [1, 4, 9, 16, 25]
print(numeros)
print('pares = list(filter(lambda x: x%2==0, numeros))')
pares = list(filter(lambda x: x%2==0, numeros))
print(pares)



print('\n\n\n')
print(f"{10*'*'} Función 'input()' {10*'*'}\n")

"""
print('Ejemplo 1:\n')
nombre = input('Ingrese su nombre: ')
print(nombre,'\n')

print('Ejemplo 2:\n')
edad = int(input('Ingrese su edad: '))
print(edad)
"""

print('\n\n\n')
print(f"{10*'*'} Función 'id()' {10*'*'}\n")

print('Ejemplo 1:\n')
numeros = [1, 4, 9, 16, 25]
print(numeros)
print('numeros_2 = numeros')
numeros_2 = numeros
print(f'Id numeros: {id(numeros)}')
print(f'Id numeros_2: {id(numeros_2)}')


print(f"{10*'*'} Funciones lambda {10*'*'}\n")


print('Ejemplo 1:\n')
print('resultado = lambda x, y: x * y')
resultado = lambda x, y: x * y
print('print(resultado(10,25))')
print(resultado(10,25))


print(f"{10*'*'} Funciones lambda con'map()' {10*'*'}\n")

print('Ejemplo 1:\n')
numeros = [1, 4, 9, 16, 25]
print(numeros)
print('cuadrados = list(map(lambda x: x ** 2, numeros))')
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados, '\n')


print('Ejemplo 2:\n')
numeros = [1, 4, 9, 16, 25]
print('numeros:', numeros)
print('cuadrado = lambda x: x ** 2')
cuadrado = lambda x: x ** 2
print('cubo = lambda x: x ** 3')
cubo = lambda x: x ** 3
print('funciones = [cuadrado, cubo]')
funciones = [cuadrado, cubo]
print('valores = [ list(map(lambda x: x(num), funciones)) for num in numeros ]')
valores = [ list(map(lambda x: x(num), funciones)) for num in numeros ]
print(valores)


print(f"{10*'*'} Funciones lambda con'filter()' {10*'*'}\n")

print('Ejemplo 1:\n')
numeros = [1, 4, 9, 16, 25]
print('numeros:', numeros)
print('pares = list(filter(lambda x: x%2==0, numeros))')
pares = list(filter(lambda x: x%2==0, numeros))
print(pares)


print(f"{10*'*'} Funciones lambda con'reduce()' {10*'*'}\n")

print('Ejemplo 1:\n')
from functools import reduce
numeros = [1, 4, 9, 16, 25]
print('numeros:', numeros)
print('suma = reduce(lambda x, y: x + y, numeros)')
suma = reduce(lambda x, y: x + y, numeros)
print(suma)
