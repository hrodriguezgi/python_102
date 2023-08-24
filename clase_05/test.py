import logging

with open('/Users/hrodriguez/Git/python_102/clase_05/archivos/ejemplo.txt', 'w') as f:
    f.writelines(['Esto es una linea escrita desde Python\n','esto es otra linea nueva\n','y esta es la última linea\n','Atte Harvey','\n'])
    print('archivo modificado')

print('fin de mi script con with')


file = open('/Users/hrodriguez/Git/python_102/clase_05/archivos/ejemplo.txt', 'a')
file.writelines(['Lineas con open\n','esto es otra linea nueva\n','y esta es la última linea\n','Atte Pedrito','\n'])
file.close()