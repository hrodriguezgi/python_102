# Diccionarios (dicts)

print(f'''
Diccionarios
------------
Los diccionarios son un tipo de dato en python que se conocen por ser iterables,
sin embargo cuentan con una diferencia notoria frente a las listas, tuplas y 
conjuntos: estos cuentan con una estructura de clave - valor. Esto quiere decir
que la información almacenada en este tipo de objetos siempre deben contar con
una llave única que los identifique en el diccionario, y cuyo valor puede ser
cualquier objeto incluyendo otro diccionario.\n''')

# Creamos varios diccionarios
dict_manz_roja = {'name':'manzana', 'color': 'rojo', 'sabor': 'dulce'}
dict_manz_verde = {'name':'manzana', 'color': 'verde', 'sabor': 'acida'}

print(f'''Los diccionarios creados son
- dict_manz_roja: {dict_manz_roja}
- dict_manz_verde: {dict_manz_verde}
''')

list_animales2 = ['serpiente', 'gorila', 'llama', 'gorila']
print(f'''Lista con elementos duplicados: {list_animales2}''')

# Métodos que se pueden realizar con los diccionarios
dict_manz_roja['tamanio'] = 'mediano' # adicionar
dict_manz_verde['sabor'] = 'dulce' # actualizar
dict_manz_roja.pop('tamanio') # eliminar


print(f'''
¿Qué podemos hacer con los diccionarios?:
- Crear nuevas llaves: dict_manz_roja['tamanio'] = 'mediano' -> {dict_manz_roja}
- Actualizar el valor de llaves: dict_manz_verde['sabor'] = 'dulce' -> {dict_manz_verde}
- Obtener el valor de una llave: dict_manz_roja['sabor'] -> {dict_manz_roja['sabor']}
- Obtener el valor de una llave: dict_manz_verde.get('tamanio') -> {dict_manz_verde.get('tamanio')} 
- Eliminar un elemento: dict_manz_roja.pop('tamanio') -> {dict_manz_roja}
- Obtener las llaves: dict_manz_verde.keys() -> {dict_manz_verde.keys()}
- Obtener los valores: dict_manz_verde.values() -> {dict_manz_verde.values()}
- Obtener los datos en tuplas: dict_manz_verde.items() -> {dict_manz_verde.items()}
''')
