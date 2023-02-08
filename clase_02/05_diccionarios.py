# Diccionarios (dicts)

print(f'''
Diccionarios
------------
Los diccionarios son un tipo de dato en python que se conocen por ser iterables,
sin embargo cuentan con una diferencia notoria frente a las listas, tuplas y 
conjuntos: estos cuentan con una estructura de clave - valor. Esto quiere decir
que la información almacenada en este tipo de objetos siempre deben contar con
una llave única que los identifique en el diccionario, y cuyo valor puede ser
cualquier objeto incluyendo otro diccionario.
''')

dict_manz_roja = {'name':'manzana', 'color': 'rojo', 'sabor': 'dulce'}
dict_manz_verde = {'name':'manzana', 'color': 'verde', 'sabor': 'acida'}

print(r"""
Vamos a crear 2 diccionarios para trabajar:
dict_manz_roja = {'name':'manzana', 'color': 'rojo', 'sabor': 'dulce'}
dict_manz_verde = {'name':'manzana', 'color': 'verde', 'sabor': 'acida'}""")

print(f"""
El resultado es el siguiente:
- dict_manz_roja: {dict_manz_roja}
- dict_manz_verde: {dict_manz_verde}
""")



dict_manz_roja['tamanio'] = 'mediano'
print(f'''
¿Qué podemos hacer con los diccionarios?:
- Crear nuevas llaves: dict_manz_roja['tamanio'] = 'mediano'
  El resultado es el siguiente -> {dict_manz_roja}
''')

dict_manz_verde['sabor'] = 'dulce'
print(f'''
- Actualizar el valor de llaves: dict_manz_verde['sabor'] = 'dulce'
  El resultado es el siguiente -> {dict_manz_verde}
''')

print(f'''
- Obtener el valor de una llave: dict_manz_roja['sabor']
  El resultado es el siguiente -> {dict_manz_roja['sabor']}
    Si la llave no existe, se genera un error.
''')

print(f'''
- Obtener el valor de una llave: dict_manz_verde.get('tamanio')
  El resultado es el siguiente -> {dict_manz_verde.get('tamanio')} 
    Si la llave no existe, no genera ningún resultado
''')

dict_manz_roja.pop('tamanio')
print(f'''
- Eliminar un elemento: dict_manz_roja.pop('tamanio')
  El resultado es el siguiente -> {dict_manz_roja}
    Si la llave no existe, genera un error.
''')

print(f'''
- Obtener las llaves: dict_manz_verde.keys()
  El resultado es el siguiente -> {dict_manz_verde.keys()}
''')

print(f'''
- Obtener los valores: dict_manz_verde.values()
  El resultado es el siguiente -> {dict_manz_verde.values()}
''')

print(f'''
- Obtener los datos en tuplas: dict_manz_verde.items()
  El resultado es el siguiente -> {dict_manz_verde.items()}
''')
