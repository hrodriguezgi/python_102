import json 
from pprint import pprint

print("""
Esto es un ejemplo del contenido de un archivo json:

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
""")

print("""
Este es otro ejemplo de un fichero json:

{
  "c": 0,
  "b": 0,
  "a": 0
}
""")


## Serialización de datos
# contamos con un objeto (lista) con datos almacenados en él
informacion = ["foo", {"bar": ["baz", None, 1.0, 2]}]

# almacenarmos la información en un fichero binario:
with open('informacion.json', 'w') as f:
    json.dump(informacion, f)



## De serialización de datos
# abrir el archivo de modo lecura y almacenamos el contenido en una variable
with open('informacion.json') as f:
    nueva_informacion = json.load(f)

print(nueva_informacion, '\n')


### json lines
# utilizando open
with open('archivos/json_lines_1.json') as f:
    lines = f.readlines()


for line in lines:
    json_object = json.loads(line)
    formated = json.dumps(json_object, indent=2)
    print(formated, '\n\n')
