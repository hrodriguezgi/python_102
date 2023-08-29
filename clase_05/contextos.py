with open('archivos/archivo.csv', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)


archivo2 = open('archivos/archivo.csv', 'r')
contenido2 = archivo2.read()
archivo2.close()
print(contenido2)

print('fin del script')