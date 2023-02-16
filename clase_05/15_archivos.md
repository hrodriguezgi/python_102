# Manipulación de ficheros con Python

Los archivos son objetos que permiten almacenar datos, por lo tanto pueden ser
manipulados desde Python para leer su contenido, modificar su contenido o para
crear contenido nuevo. 

Para llevar a cabo esto, se requiere:
- Abrir un archivo
- Leer/Escribir
- Cerrar el archivo.

Python nos permite realizar las anteriores acciones de la siguiente forma:

## Apertura de un archivo
`open` es la función que utilizaremos para la apertura de archivos en python. 
Esta función tiene entre sus parámetros lo siguiente:

- `file`: nombre del archivo que queremos abrir
- `mode`: esto nos permite definir si el archivo lo deseamos leer, modificar
o crear
- `encoding`: para indicarle a python la codificación en la que se encuentra el
archivo y la lectura de los caracteres sea correcta

Algunos de los argumentos son los siguientes:

```python
open(file, mode='r', encoding=None, errors=None, newline=None)
```

Si tenemos un archivo llamado file.txt la forma de abrirlo para leer su
contenido será:

```python
file = open('file.txt')
```

Al ver el comando anterior, vemos que el parámetro `mode` no fue enviado y esto
se debe a que por defecto el utiliza el valor de `r`, que significa en modo de
letura. Sin embargo otros valores que pueden ser utilizados son los siguientes:

| Caracter | Descripción |
|----------|-------------|
| `'r'`    | Sólo lectura.
| `'w'`    | Abrir un archivo para escritura. Si el archivo no existe se crea, si existe se sobre escribe.
| `'x'`    | Abrir un archivo para creación. Si el archivo existe la operación falla.
| `'a'`    | Abrir el archivo para adicionar datos al final del mismo. Si el archivo no existe se crea
| `'b'`    | Abrir el archivo en modo binario
| `'t'`    | Abrir el archivo en modo texto
| `'+'`    | Abrir un archivo para actualizar (leer y escribir)

Algunos ejemplos son:

```python
# abrir el archivo
archivo = open('archivos/archivo.txt', 'r')
```

## Cierre del archivo
Es muy importante que todo archivo que abrimos en python lo cerremos, debido a
que en el momento de la apertura estamos utilizando recursos para esta acción,
por lo que cerrar el archivo será la forma de liberarlos. Esto se llevará a
cabo con la función `close` así:

```python
archivo.close()
```


## Lectura/Escritura del archivo
Python cuenta con diferentes métodos para llevar a cabo la lectura/escritura del
contenido de un archivo:

### Lectura

#### `read()`
Este método retorna todo el contenido del archivo abierto previamente. Ejemplo:

```python
>>> archivo = open('archivos/archivo.txt', 'r')
>>> contenido = archivo.read()
>>> print(contenido)
Los archivos son objetos que permiten almacenar datos, por lo tanto pueden ser
manipulados desde Python para leer su contenido, modificar su contenido o para
crear contenido nuevo. 

Para llevar a cabo esto, se requiere:
- Abrir un archivo
- Leer/Escribir
- Cerrar el archivo.
>>> archivo.close()
```

#### `read(X)`
Este método retorna los `X` carácteres del contenido del archivo abierto
previamente. Ejemplo:

```python
>>> archivo = open('archivos/archivo.txt', 'r')
>>> contenido = archivo.read(10)
>>> print(contenido)
Los archiv
>>> archivo.close()
```

#### `readline`
Este método retorna cada una de la línea del contenido del archivo abierto
previamente. Ejemplo:

```python
>>> archivo = open('archivos/archivo.txt', 'r')
>>> contenido = archivo.readline()
>>> print(contenido)
Los archivos son objetos que permiten almacenar datos, por lo tanto pueden ser

```

#### `readlines`
Este método retorna una lista donde cada elemento de ella será cada línea del
archivo abierto previamente. Ejemplo:

```python
>>> archivo = open('archivos/archivo.txt', 'r')
>>> contenido = archivo.readlines()
>>> print(contenido)
['Los archivos son objetos que permiten almacenar datos, por lo tanto pueden ser\n',
 'manipulados desde Python para leer su contenido, modificar su contenido o para\n',
 'crear contenido nuevo. \n',
 '\n',
 'Para llevar a cabo esto, se requiere:\n',
 '- Abrir un archivo\n',
 '- Leer/Escribir\n',
 '- Cerrar el archivo.']
>>> archivo.close()
```

### Escritura

#### `write()`
Este método permite escribir un string a un archivo. Se debe tener en cuenta
cómo se desea realizar la operación:

- Escritura con el modo `'w'`

```python
>>> archivo = open('archivos/nuevo_archivo.txt', 'w')
>>> archivo.write('''Esto es una linea escrita desde Python, si el archivo
tenía información antes, esta ha sido sobre escrita
''')
>>> archivo.close()
```

- Escritura con el modo `'a'`

```python
>>> archivo = open('archivos/nuevo_archivo.txt', 'a')
>>> archivo.write('''Esto es otra linea escrita desde Python, y que es adicionada
al final del archivo, si este no existe será creado''')
>>> archivo.close()
```

#### `writelines`
Este método permite escribir una lista a un archivo. Se debe tener en cuenta
cómo se desea realizar la operación:

- Escritura con el modo `'w'`

```python
>>> archivo = open('archivos/nuevo_archivo.txt', 'w')
>>> archivo.writelines(['Esto es una linea escrita desde Python',
'esto es otra linea nueva',
'y esta es la última linea'])
>>> archivo.close()
```

- Escritura con el modo `'a'`

```python
>>> archivo = open('archivos/nuevo_archivo.txt', 'a')
>>> archivo.writelines(['Esta es un nuevo texto al final',
'Y este si es el final'])
>>> archivo.close()
```

## Otra forma de abrir archivos: with - open
Dado que durante el código se puede en algunas ocasiones realizar el cierre
adecuado del archivo, en Python contamos con la sentencia `with... open` que
permite cerrar el archivo de forma automática una vez las acciones que queremos
realizar han sido completadas. 

La sintaxis es la siguiente:

```python
with open('archivos/archivo.csv', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)
```
