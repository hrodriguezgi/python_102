# Listas (lists)

print(f'''
Listas
------
Las listas son un tipo de dato en python que se conocen por ser iterables
como lo son los conjuntos y las tuplas. Este tipo de dato permite almacenar
cualquier otro tipo de dato, incluso otras listas. Son mutables, son indexables 
(slice) y permiten datos duplicados.\n''')

# Creamos varias listas
list_frutas = ['manzana', 'banano', 'naranja']
list_animales = ['serpiente', 'gorila', 'llama']

print(f'''Las listas creadas son:
- list_frutas: {list_frutas}
- list_animales: {list_animales}
''')

list_animales2 = ['serpiente', 'gorila', 'llama', 'gorila', 'caballo', 'vaca', 'serpiente', 'llama']
print(f'''Lista con elementos duplicados: {list_animales2}''')

# Métodos que se pueden realizar con las listas
list_animales.append('caballo') # append
list_frutas.insert(3, 'zanahoria') # insert
list_animales2.pop(3) # pop
list_animales2.remove('serpiente') # remove
list_frutas.extend(list_animales) # extend
list_frutas_copy = list_frutas.copy() # copy

print(f'''
¿Qué podemos hacer con las listas?:
- Slice: list_frutas[:2] -> {list_frutas[:2]}
- Append: list_animales.append('vaca') -> {list_animales}
- Insert: list_frutas.insert(3, 'zanahoria') -> {list_frutas}
- Pop: list_animales2.pop(3) -> {list_animales2}
- Remove: list_animales2.remove('serpiente') -> {list_animales2}
- Extend: list_frutas.extend(list_animales) -> {list_frutas}
- Count: list_frutas.count() -> {list_animales2.count('llama')}
- Copy: list_frutas_copy = list_frutas.copy() -> {list_frutas_copy}
''')

