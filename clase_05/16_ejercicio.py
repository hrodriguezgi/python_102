# Crear un script en python que permita responder cada uno de los siguientes
# puntos a partir del archivo ejercicio.txt
# 1. Cuál es la cantidad de veces que aparece cada una de las palabras en el
#    texto. Esto debe quedar almacenado en un diccionario
# 2. Cuál es la frecuencia de cada una de las palabras que contienen 2 letras.
#    Esto debe quedar almacenado en un diccionario
# 3. Cuál es la linea qué más palabras contiene? Imprimir dicha linea y la
#    cantidad de palabras
# 4. Cuál es la linea qué más palabras de 3 letras contiene? Imprimir dicha
#    linea y la cantidad de palabras
# 5. Cree un archivo nuevo donde se almacene cada una de las líneas del archivo
#    original eliminando cada una de las palabras con 4 o letras menos. El
#    archivo destino se llamará ejercicio_mod.txt

# Nota: No olvidar remover caracteres especiales para el conteo de las palabras
# y estandarizar las palabras


from pprint import pprint

# Punto 1
with open('/Users/hrodriguez/Git/python_102/clase_05/archivos/ejercicio.txt') as var:
    # leo el contenido del archivo y lo almaceno en contenido
    contenido = var.read()

# remplazo los caracteres
contenido = contenido.replace(",", "").\
                      replace("-", "").\
                      replace("'", "").\
                      replace('(', '').\
                      replace(')', '').\
                      replace('.', '')

# llevo el contenido del string a una lista
contenido = contenido.lower().split()
# Creo mi diccionario vacío
conteo_palabras = dict()
# palabras unicas
palabras_unicas = set(contenido)
# Recorro la lista y almaceno en el diccionario la frecuencia de cada palabra
for palabra in palabras_unicas:
    num = contenido.count(palabra)
    conteo_palabras[palabra] = num

pprint(f'Punto 1: {conteo_palabras}')
print()

# Diccionario para el punto 2
conteo_palabras_2_letras = dict()
# Recorro la lista y almaceno en el diccionario la frecuencia de cada palabra
for palabra in palabras_unicas:
    if len(palabra) == 2:
        num = contenido.count(palabra)
        conteo_palabras_2_letras[palabra] = num

pprint(f'Punto 2: {conteo_palabras_2_letras}')

# Punto 3
import re

with open('/Users/hrodriguez/Git/python_102/clase_05/archivos/ejercicio.txt') as var:
    # leo el contenido del archivo y lo almaceno en contenido
    contenido_lineas = var.readlines() #-> devuelve una lista

maximo = 0
lista_punto_3 = ""

for idx, linea in enumerate(contenido_lineas):
    linea = re.sub(r'[^a-zA-Z0-9]', ' ', linea)
    linea = linea.split()
    conteo = len(linea)
    if conteo > maximo:
        maximo = conteo
        lista_punto_3 = " ".join(linea)

print(f'la linea: {lista_punto_3} es la que contiene mayor cantidad de palabras: {maximo}')
#print(f'la linea: {contenido_lineas[lista_punto_3]} es la que contiene mayor cantidad de palabras: {maximo}')


# Punto 4
maximo = 0
lista_punto_3 = ""


for idx, linea in enumerate(contenido_lineas):
    linea = re.sub(r'[^a-zA-Z0-9]', ' ', linea)
    linea = linea.split()
    conteo = 0
    for palabra in linea:
        if len(palabra) == 3:
            conteo += 1
    if conteo > maximo:
        maximo = conteo
        lista_punto_3 = " ".join(linea)



print(f'la linea: {lista_punto_3} es la que contiene mayor cantidad de palabras de tres letras: {maximo}')


# Punto 5
maximo = 0
lista_punto_3 = ""

nueva_contenido_lineas = []

for idx, linea in enumerate(contenido_lineas):
    linea = re.sub(r'[^a-zA-Z0-9]', ' ', linea)
    linea = linea.split()
    nueva_lista = []
    for palabra in linea:
        if len(palabra) > 4:
            nueva_lista.append(palabra)
    nueva_contenido_lineas.append(" ".join(nueva_lista) + '\n')

print()
print(f'{" ".join(nueva_contenido_lineas)}')