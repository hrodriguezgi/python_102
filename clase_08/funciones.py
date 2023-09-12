def mi_primera_funcion():
    print('Hola mundo')

mi_primera_funcion()


def multiplicado(valor:int, valor2:int, valor3:float):
    """
    Esta función realiza la multiplicación de sus argumentos
    valor: dato de tipo entero
    valor2: dato de tipo entero
    valor2: dato de tipo entero
    valor3: dato de tipo flotante
    resultado: dato de tipo entero
    """
    resultado =  valor * valor2 * valor3
    return resultado


print(multiplicado(10,20,30))


resultado = lambda x, y, z: x * y * z
print(resultado(1, 2, 3))
print()


def cuadrados(x):
    return x ** 2


numeros = [1, 4, 9, 16, 25]
print(list(map(lambda x: x ** 2, numeros)))

numeros2 = [1, 2, 3, 4, 5]
print(list(map(cuadrados, numeros2)))

numeros3 = [2, 4, 6, 8, 10]
print([ x ** 2 for x in numeros3 ])
print()



numeros = [1, 4, 9, 16, 25]
print(list(filter(lambda x: x%2==0, numeros)))

print([ x for x in numeros if x%2==0 ])
print()


from functools import reduce
numeros = [1, 4, 9, 16, 25]
print(reduce(lambda x, y: x * y, numeros))

y = 0
[y := y + x for x in numeros] # Walrus Operator
print(y)
