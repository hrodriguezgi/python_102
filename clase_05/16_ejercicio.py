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
    contenido_lineas = var.readlines()
    # remplazo los caracteres
    contenido.replace(",", "").replace("-", "").replace("'", "").replace('(', '').replace(')', '')
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

pprint(conteo_palabras)
