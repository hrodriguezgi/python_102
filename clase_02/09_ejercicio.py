# Strings

variable = 'appname=pythonbancolombia.corp'

# 1. Se requiere crear una variable que almacene el valor de appname, 
#    pythonbancolombia y corp: utilizando slice

var_nombre = variable[ : variable.index('=')]
var_python = variable[variable.index('=')+1 : variable.index('.')]
var_corp = variable[variable.index('.')+1 : ]

print(f'var_nombre: {var_nombre}')
print(f'var_python: {var_python}')
print(f'var_corp: {var_corp}')
print('')

# 2. Se requiere identificar el índice de '=', '.' y '/'

print(f"indice de '=': {variable.find('=')}")
print(f"indice de '.': {variable.find('.')}")
print(f"indice de '/': {variable.find('/')}")
print()

# Conjuntos

elementos = '1 2 3 4 5 6 7 8 8 8 8 8'

# 3. A partir del anterior string, construir una lista con los elementos únicos
nueva_lista = list(set(elementos.split()))
print(nueva_lista, type(nueva_lista))
print('')

# 4. Del siguiente string, se debe crear una lista con todos los carácteres
#    (sin distinguir mayusculas y minúsculas) ordenados alfabeticamente.

texto = """
Hola, El dia de hoy es 7 de FEBRERO del 2023. Estamos realizaNDO un
rePAso de lo que podemoS haCEr en PythoN.
"""

alfabeto = [ caracter for caracter in texto ]
alfabeto.sort()
print(alfabeto)
print('')

palabras = texto.split()
print(palabras)
