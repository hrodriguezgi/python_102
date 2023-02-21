# Manipulación de ficheros con Python

Otro de los formatos que son frecuentemente utilizados en la actualidad y en la
industria son los ficheros JSON. Este tipo de archivos que vienen de JavaScript
Object Notation, es un formato estándar que es utilizado para enviar información
entre apliaciones web y un servidor. A diferencia de los archivos pickle, estos
pueden ser leídos y comprendidos desde un editor de texto.

Esto es un ejemplo  de un archivo json:

```json
[
  "foo",
  {
    "bar": [
      "baz",
      null,
      1.0,
      2
    ]
  }
]
```

Y también este otro:

```json
{
  "c": 0,
  "b": 0,
  "a": 0
}
```

Python cuenta con un módulo llamado `json` que permite leer y modificar el
contenido ya sea de un fichero o de una variable.

## Serialización de datos

Dado que es un módulo, siempre debemos realizar la importación de este al inicio
de nuestro script para que python pueda comprender los comandos que escribamos
haciendo uso de las funciones propias de dicho módulo.

```python
import json

# contamos con un objeto (lista) con datos almacenados en él
informacion = ["foo", {"bar": ["baz", None, 1.0, 2]}]

# almacenarmos la información en un fichero binario:
with open('informacion.json', 'w') as f:
    json.dump(informacion, f)
```

Con lo anterior hemos construido un fichero que cuenta con nuestra información
pero serializada con ayuda de `json`. Si vemos el resultado esto es lo que
tenemos:

```sh
user@localhost $ cat informacion.json
["foo", {"bar": ["baz", null, 1.0, 2]}]
```

Como puedes ver, hay una ligera diferencia en los datos, y es que en nuestra
variable original teníamos un dato con valor `None`, y en el archivo creado este
valor aparece como `null` y esto se debe a que json hace la siguiente conversión:

| **Python** | **Json** |
|--------|------|
| `dict`   | `object`
| `list`, `tuple` | `array`
| `str` | `string`
| `int`, `float` | `number`
| `True` | `true`
| `False` | `false`
| `None` | `null`


## De serialización de datos

Una vez ya tenemos la información almacenada en un archivo json, la forma en
como lo vamos a leer desde python será de serializando el contenido y para esto
lo haremos de la siguiente forma:

```python
import json

# abrir el archivo de modo lecura y almacenamos el contenido en una variable
with open('informacion.json') as f:
    nueva_informacion = json.load(f)

print(nueva_informacion)
```

### Funciones de `json`

- `dump`: escribe el contenido de un objeto a un archivo.
    - `json.dump(obj, file)`
- `dumps`: genera la representación de un objeto en json y lo retorna
    - `json.dumps(obj)`
- `load`: lee un objeto serializado a partir de un archivo
    - `json.load(file)`
- `loads`: lee la información de una variable que contiene datos en formato json y lo retorna
    - `json.loads(data)`

## Caso especial

Hay algunos archivos JSON que son conocidos como json lines, lo cual significa
que en un archivo, cada linea es un objeto json totalmente independiente a la
siguiente linea.

Lo siguiente es un ejemplo de este tipo de ficheros:

```python
{"votes": {"funny": 2, "useful": 5, "cool": 1}, "user_id": "peter", "average_stars": 3.5, "review_count": 12}
{"votes": {"funny": 1, "useful": 2, "cool": 4}, "user_id": "paul", "average_stars": 3.5, "review_count": 12}
{"votes": {"funny": 1, "useful": 0, "cool": 4}, "user_id": "ktags", "average_stars": 3.5, "review_count": 12}
{"votes": {"funny": 6, "useful": 5, "cool": 0}, "user_id": "fulaz", "average_stars": 3.5, "review_count": 12}
{"votes": {"funny": 1, "useful": 8, "cool": 2}, "user_id": "sandy", "average_stars": 3.5, "review_count": 12}
```

Para leer este tipo de ficheros tendremos alternativas como:
- Utilizar la función `readlines()` de `open`
- Utilizar la función `reader` de la librería librería `jsonlines`
- Utilizar la función `read_json()` de la librería de `pandas`

Ejemplos:

- `open`:

```python
data = []
with open('json_file.json') as f:
    lines = f.readlines()
    data.append(lines)
```

- `jsonlines`:

```python
import jsonlines

data = []
with jsonlines.open('json_file.json') as f:
    for line in f:
        data.append(line)
```

- `pandas`:

```python
import pandas

df = pandas.read_json('json_file.json', lines=True)
```