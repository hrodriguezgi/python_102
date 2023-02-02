from pprint import pprint

# Para crear dinámicamente un diccionario podemos hacer uso de un loop: for

print('Sintaxis de un for:\n')
print(f'for element in iterable:')
print(f'\tactions\n')

print(f'Ejemplo:')
print(f'for numero in range(1, 11):')
print(r'  dict[f"numero_{numero}"] = numero')
print()

numeros_dict = {}

for num in range(1, 10):
  numeros_dict[f'num_{num}'] = num
print(f'lista numeros:')
pprint(numeros_dict)

print(f'\n\n{20*"*"}\n\n')


# Haciendo uso de dict comprehension
print('Sintaxis de un dict comprehension:')
print(r'variable = {key:value for var in iterable}')
print()

print(f'Ejemplo:')
print(r'numeros_dict_2 = {f"num_{numero}":numero for numero in range(11, 21)]')
print()

numeros_dict_2 = {}

numeros_dict_2 = {f'num_{numero}': numero * 2 for numero in range(11, 21)}

print(f'lista numeros:')
pprint(numeros_dict_2)

print(f'\n\n{20*"*"}\n\n')


# Dict comprehension a partir de zip
deportes = ['futbol', 'baloncesto', 'tenis', 'ajedrez']
jugadores = [22, 5, 2, 1]

deportes_dict = {
  deporte: jugador
  for (deporte, jugador) in zip(deportes, jugadores)
}

pprint(deportes_dict)
print(f'\n\n{20*"*"}\n\n')


# Condiciones en dict comprehension
print('Sintaxis de un dict comprehension con condicion:')
print(f'variable = [key:value for var in iterable if condition]\n')

print(f'Ejemplo:')
print(f'numeros_3 = [numero for numero in range(11, 21) if numero % 2 == 0]\n')

deportes_multijugador = {deporte: jugador for deporte, jugador in zip(deportes, jugadores) if jugador > 3}

pprint(deportes_multijugador)