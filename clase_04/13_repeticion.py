"""
# for
lista = [1, 2, 3, 4, 5]
for num in lista:
    j = num**2
    k = j + 10
    print(f'el cuadrado de {num} es {j}')
    print(f' y la suma es {k}')
    if j % 2 == 0:
        print(' y ademas es par')
    else:
        print(' es impar')
"""


# for
diccionario = {"colombia": "peso", "peru": "sol", "venezuela": "bolivar"}

"""
iter = 1

for pais, moneda in diccionario.items(): # me retorna tuplas de (llave, valor)
    print(f'iteracion {iter}: el pais es {pais} y su moneda es {moneda}')
    iter += 1
"""

# Quiero modificar la moneda del pais ven por bolivares
# Alternativa: diccionario['ven'] = 'bolivares'

"""
for pais, moneda in diccionario.items():
    print(pais)
    if pais == 'venezuela':
        diccionario[pais] = 'bolivares'

print(diccionario)
"""

"""
# for con enumerate en lista
lista = [10,20,30,40,50]

for index, value in enumerate(lista): # -> retorna tuplas de (index, value)
    print(index, value)
    if index == 2:
        lista[index] = value * 10

print(lista)
# lista = [10,20,10,40,50]
"""

"""
# for con enumerate en diccionario
for ind, pais in enumerate(diccionario):
    print(f'el valor del indice es {ind} y el pais es {pais}')

"""

"""
# for en tuplas
tupla = (10,20,30,40,50)

for idx, num in enumerate(tupla):
    print(idx, num)
"""


# while
a = 5
b = 0
itera = 1
while b < a:
    print(f"el valor de b es: {b}")
    print(" hola mundo")
    print(" otro hola mundo")
    b += 1
