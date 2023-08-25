# Apertura de un archivo


"""
# Método read()
# Abro el archivo
archivo = open('archivos/ejemplo.txt')
print(type(archivo))
# Manipulo
contenido = archivo.read()
# Cierro el archivo
archivo.close()

print(contenido)
"""

"""
# Método readline()
# Abro el archivo
archivo = open('archivos/ejemplo.txt')
# Manipulo
contenido = archivo.readline()
print(type(contenido), contenido)
contenido = archivo.readline()
print(type(contenido), contenido)
contenido = archivo.readline()
print(type(contenido), contenido)
# Cierro el archivo
archivo.close()
"""

"""
# Método readlines()
# Abro el archivo
archivo = open('archivos/ejemplo.txt')
# Manipulo
contenido = archivo.readlines()
print(type(contenido))
print(contenido)
print(len(contenido))
# Cierro el archivo
archivo.close()
"""