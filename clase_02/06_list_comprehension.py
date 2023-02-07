# Para crear dinámicamente una lista podemos hacer uso de un loop: for

print('Sintaxis de un for:\n')
print(f'for element in iterable:')
print(f'\tactions\n')

print(f'Ejemplo:')
print(f'for numero in range(1, 11):')
print(f'\tnumeros.append(numero)\n')

numeros = []
print(f'lista numeros: {numeros}')

for numero in range(1, 11):
  numeros.append(numero)

print(f'lista numeros: {numeros}')

print(f'\n\n{20*"*"}\n\n')

# Haciendo uso de list comprehension
print('Sintaxis de un list comprehension:')
print(f'variable = [element for element in iterable]\n')

print(f'Ejemplo:')
print(f'numeros_2 = [numero for numero in range(11, 21)]\n')

numeros_2 = []
print(f'lista numeros: {numeros_2}')

numeros_2 = [numero for numero in range(11, 21)]

print(f'lista numeros: {numeros_2}')

print(f'\n\n{20*"*"}\n\n')

# Condiciones en list comprehension
print('Sintaxis de un list comprehension con condicion:')
print(f'variable = [element for element in iterable if condition]\n')

print(f'Ejemplo:')
print(f'numeros_3 = [numero for numero in range(11, 21) if numero % 2 == 0]\n')

numeros_3 = []
numeros_3 = [numero for numero in range(21, 31) if numero % 2 == 0]

print(f'lista numeros: {numeros_3}')