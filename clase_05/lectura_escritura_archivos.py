
# Abrimos el archivo en modo lectura y escritura
archivo = open('archivos/lectura_escritura.txt', 'r+')

# Leo el contenido actual
contenido = archivo.read()
print('1', contenido)

# Escribo un nuevo contenido
nuevo_contenido = ['Estas son las mañanitas\n',
                   'que cantaba el rey David\n']
archivo.writelines(nuevo_contenido)

# Leo el contenido actual?
contenido = archivo.read()
print('2', contenido)

# Cerramos para persistir los cambios
archivo.close()

archivo = open('archivos/lectura_escritura.txt', 'r+')
contenido = archivo.read()
print('3', contenido)