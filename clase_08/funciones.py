def mi_primera_funcion():
    print('Hola mundo')

mi_primera_funcion()


def multiplicado(valor, valor2, valor3):
    resultado =  valor * valor2 * valor3
    return resultado


print(multiplicado(10, 20, 30))


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