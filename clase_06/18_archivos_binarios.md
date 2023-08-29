# Manipulación de ficheros con Python

Como lo vimos en la sesión pasada, python cuenta con una función (`open`) que
nos permite realizar la apertura de archivos para su lectura y/o modificación.
Por otro lado Python cuenta con un módulo llamado `pickle`, que permite realizar
serialización y de-seriaización que en conjunto con la función `open` podremos
realizar manipulación de ficheros binarios.

Para llevar a cabo esto, basta con abrir un archivo donde queremos almacenar
nuestro contenido serializado, o donde se encuentre nuestra información ya
serializada para su lectura. Para esto veremos dos ejemplos:

## Serialización de datos

Dado que `pickle` es un módulo, lo primero que debemos hacer en nuestro script
de Python es importar la librería: `import pickle` y posteriormente realizar
nuestro objetivo.

```python
import pickle

# contamos con un diccionario con datos almacenados en él
informacion = {
    'id': 1,
    'nombres': 'Harvey',
    'apellidos': 'Rodriguez',
    'telefono': 12345678,
    'ciudad': 'Envigado'
}

# almacenarmos la información en un fichero binario:
with open('info_serial.pickle', 'wb') as f:
    pickle.dump(informacion, f)
```

Con lo anterior hemos construido un fichero que cuenta con nuestra información
pero serializada con ayuda de `pickle`.


## De serialización de datos

Una vez ya tenemos la información serializada, la forma en como lo vamos a leer
es de serializando el contenido y para esto lo haremos de la siguiente forma:

```python
import pickle

# abrir el archivo de modo lecura y almacenamos el contenido en una variable
with open('info_serial.pickle', 'rb') as f:
    nueva_informacion = pickle.load(f)

print(nueva_informacion)
```

### Funciones de `pickle`

- `dump`: escribe la serialización de un objeto a un archivo.
    - `pickle.dump(obj, file)`
- `dumps`: genera la serialización de un objeto y lo retorna
    - `pickle.dumps(obj)`
- `load`: lee un objeto serializado a partir de un archivo
    - `pickle.load(file)`
- `loads`: genera la de serialización de un objeto previamente serializado y lo retorna
    - `pickle.loads(data)`
