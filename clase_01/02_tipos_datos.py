print('Tipos de datos en python:')
print('- Numéricos: int, float, complex')
v_int = 20
print(type(v_int), v_int)

v_float = 3.14
print(type(v_float), v_float)

v_complex = 2 + 5j
print(type(v_complex), v_complex)

print('\n- Texto: str')
v_str = 'Hello World'
print(type(v_str), v_str)

print('\n- Booleanos: bool')
v_bool = True
print(type(v_bool), v_bool)

print('\n- Secuencias: list, tuple, range')
v_list = ["apple", "banana", "cherry"]
print(type(v_list), v_list)

v_tuple = ("apple", "banana", "cherry")
print(type(v_tuple), v_tuple)

v_range = range(6)
print(type(v_range), v_range)

print('\n- Mapeo: dict (llave, valor)')
v_dict = {"name": "John", "age": 36}
print(type(v_dict), v_dict)

print('\n- Conjuntos: set')
v_set = {"apple", "banana", "cherry"}
print(type(v_set), v_set)
