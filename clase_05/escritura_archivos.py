# Apertura de un archivo


"""
# Método write()
# Abro el archivo
archivo = open('archivos/en_clase.txt', 'w')
# Manipulo
contenido = "Esto es un mensaje enviado desde python a un archivo\n"
archivo.write(contenido)
# Cierro el archivo
archivo.close()

# Abro el archivo
archivo = open('archivos/en_clase.txt', 'a')
# Manipulo
contenido = "Esto es una nueva linea en el archivo"
archivo.write(contenido)
# Cierro el archivo
archivo.close()
"""

# Método writelines()
# Abro el archivo
archivo = open('archivos/en_clase.txt', 'w')
# Manipulo
contenido = ["Esto es un mensaje enviado desde python a un archivo\n",
             "Hola mundo\n",
             "esta es la tercera linea\n",
             'última linea\n']
archivo.writelines(contenido)
# Cierro el archivo
archivo.close()

archivo = open('archivos/en_clase.txt', 'a')
# Manipulo
contenido = ["\n",
             "estas otras lineas son adicionadas con append\n"]
archivo.writelines(contenido)
# Cierro el archivo
archivo.close()