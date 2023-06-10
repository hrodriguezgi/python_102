# Ejercicios

# DUMPS
# 1. Convertir el siguiente objeto en un json e imprimirlo utilizando una
# identacion de 2 espacios:

carros = [{
    'referencia': 'Rav4',
    'marca': 'Toyota',
    'cilindraje': '2500 cc',
    'modelo': 2020,
    'precio': 32000,
    'nuevo': False
    },
    {
    'referencia': 'Niro',
    'marca': 'KIA',
    'cilindraje': '1600 cc',
    'precio': 15000,
    'nuevo': True
    }]


import json

carros_json = json.dumps(carros, indent=2)
print(carros_json)


# LOAD
# 2. A partir del archivo 20_ejercicio.json responder las siguientes preguntas:
# a. Cuál es el nombre de la persona que mayor balance tiene?
# b. Cuántos hombres y mujeres hay en el archivo?
# c. El usuario Elsie Lowery se encuentra activo?
# d. Cuál es la frecuencia de repetición de las frutas
# e. Cuál es el promedio de edad de los usuarios

import jsonlines

data = []
with jsonlines.open('/Users/hrodriguez/Git/python_102/clase_06/archivos/20_ejercicio.json') as f:
    for line in f:
        data.append(line)

# a. Cuál es el nombre de la persona que mayor balance tiene?
maximo = 0
nombre = ''
for elemento in data:
    balance = float(elemento.get('balance').replace('$','').replace(',',''))
    if balance > maximo:
        maximo = balance
        nombre = elemento.get('name')

print(nombre)

# b. Cuántos hombres y mujeres hay en el archivo?
hombres = 0
mujeres = 0
for elemento in data:
    if elemento.get('gender') == 'male':
        hombres = hombres + 1
    else:
        mujeres = mujeres + 1

print(f'hombres: {hombres}, mujeres: {mujeres}')


# c. El usuario Elsie Lowery se encuentra activo?
for elemento in data:
    if elemento.get('name') == 'Elsie Lowery' and elemento.get('isActive'):
        print('Usuario activo')
    elif elemento.get('name') == 'Elsie Lowery' and not elemento.get('isActive'):
        print('Usuario inactivo')


# d. Cuál es la frecuencia de repetición de las frutas
frutas = {}
for elemento in data:
    fruta = elemento.get('favoriteFruit')
    frutas[fruta] = frutas.get(fruta, 0) + 1

print(frutas)


# e. Cuál es el promedio de edad de los usuarios
# promedio = suma de todos los valores dividido por el total de valores
# promedio = sumatoria / elementos
sumatoria = 0
elementos = 0

for elememto in data:
    sumatoria += elemento.get('age')
    elementos += 1

print(sumatoria/elementos)

# DUMP
# 3. Almacenar la información del archivo anterior en un archivo nuevo donde
# solo se almacenen las siguientes llaves, tener en cuenta que debe ser un
# archivo json estándar:
# idx, isActive, name, email.

data_2 = []
campos = ['idx', 'isActive', 'name', 'email']

for elemento in data:
    dictionary = {}
    for campo in campos:
        dictionary[campo] = elemento.get(campo)
    data_2.append(dictionary)

with open('/Users/hrodriguez/Git/python_102/clase_06/archivos/20_ejercicio_nuevo.json', 'w') as f:
    json.dump(data_2, f, indent=2)