# Listas (lists)

print(f'''
Listas
------
Las listas son un tipo de dato en python que se conocen por ser iterables
como lo son los conjuntos y las tuplas. Este tipo de dato permite almacenar
cualquier otro tipo de dato, incluso otras listas. Son mutables, son indexables 
(slice) y permiten datos duplicados.''')

# Creamos varias listas
list_frutas = ['manzana', 'banano', 'naranja']
list_animales = ['serpiente', 'gorila', 'llama']

print(f'''
Creamos las siguientes listas:

- list_frutas = ['manzana', 'banano', 'naranja']
- list_animales = ['serpiente', 'gorila', 'llama']

El resultado es:

- list_frutas: {list_frutas}
- list_animales: {list_animales}''')


list_animales2 = ['serpiente', 'gorila', 'llama', 'gorila', 'caballo', 'vaca', 'serpiente', 'llama']

print(f'''
Como se mencionó antes, las listas permiten elementos duplicados. Vamos a crear
la siguiente lista:

list_animales2 = ['serpiente', 'gorila', 'llama', 'gorila', 'caballo', 'vaca', 'serpiente', 'llama']

El resultado es el siguiente:

- list_animales2: {list_animales2}''')


# Lista creada durante la clase:
list_animales2_new = ['serpiente', 'gorila', 'llama', 'Gorila', 'caballo', 'vaca', 'Serpiente', 'Llama']
print(f'''
Ahora vamos a crear una lista con la que vamos a revisar algunos de los métodos
de las listas:

list_animales2_new = ['serpiente', 'gorila', 'llama', 'Gorila', 'caballo', 'vaca', 'Serpiente', 'Llama']

Es necesario aclarar que esta lista no tiene (al menos por ahora) elementos
duplicados ya que a pesar de tener 'serpiente' y 'Serpiente' son dos objetos
completamente diferentes. El resultado es esta lista:

- list_animales2_new: {list_animales2_new}''')

print(f'''
¿Qué podemos hacer con las listas?:
- Slice: list_animales2_new[::2] -> {list_animales2_new[::2]}
   slice: [inicio:fin:salto]
    si no está definido el inicio, se toma 0 como valor por defecto
    si no está definido el fin, se toma desde el valor definido en inicio hasta el final de la lista.
''')

list_animales2_new.append('vaca')
print(f'''
- Append: list_animales2_new.append('vaca') -> {list_animales2_new}
''')

list_animales2_new.insert(4, 'Aguila')
print(f'''
- Insert: list_animales2_new.insert(4, 'Aguila') -> {list_animales2_new}
''')

list_animales2_new.pop(3)
print(f'''
- Pop: list_animales2_new.pop(3) -> {list_animales2_new}
''')

list_animales2_new.remove('vaca')
print(f'''
- Remove: list_animales2_new.remove('vaca') -> {list_animales2_new}
''')

otros_animales = ['hipopotamo', 'jirafa', 'Aguila']
list_animales2_new.extend(otros_animales)
print(f'''
- Extend: list_animales2_new.extend(otros_animales) -> {list_animales2_new}
''')

print(f'''
- Count: list_animales2_new.count('Vaca') -> {list_animales2_new.count('Vaca')}
''')

list_animales2_new_copy = list_animales2_new.copy()
print(f'''
- Copy: list_animales2_new_copy = list_animales2_new.copy() -> {list_animales2_new_copy}
''')
