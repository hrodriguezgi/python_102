import json


# Esto es un diccionario común y corriente
mi_diccionario = {
  "c": True,
  "b": False,
  "a": (1,2,3,4),
  "d": 'Hola mundo'
}

print(type(mi_diccionario), mi_diccionario)

# Para convertir el diccionario a un archivo json utilizo dump
with open('mi_archivo.json', 'w') as variable_archivo:
    json.dump(mi_diccionario, variable_archivo)


# Para leer el archivo json e imprimirlo en Python utilizamos load
with open('mi_archivo.json', 'r') as archivo_externo:
    nuevo_diccionario = json.load(archivo_externo)

print(nuevo_diccionario)