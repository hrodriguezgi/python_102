# Convertir el siguiente objeto en un json e imprimirlo utilizando
# una identacion de 2 espacios:

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


# A partir del archivo adjunto llamado 20_ejercicio.json responder las siguientes preguntas:
# Cuál es el nombre de la persona que mayor balance tiene? 
# Cuántos hombres y mujeres hay en el archivo?
# El usuario Elsie Lowery se encuentra activo?
# Cuál es la frecuencia de repetición de las frutas
# Cuál es el promedio de edad de los usuarios


# Almacenar la información del archivo anterior en un archivo nuevo donde solo
# se almacenen las siguientes llaves, tener en cuenta que debe ser un archivo json estándar:
# idx, isActive, name, email.
# El nombre del archivo será 20_ejercicio_salida.json

import json 

with open('20_ejercicio.json') as file:
    content = file.readlines()

columns = ['idx', 'isActive', 'name', 'email']

content_json = list()
for line in content:
    tmp_dict = dict()
    new_line = json.loads(line)
    for column in columns:
        tmp_dict[column] = new_line.get(column)
    content_json.append(tmp_dict)

with open('20_ejercicio_salida.json', 'w') as file:
    json.dump(content_json, file, indent=2)
