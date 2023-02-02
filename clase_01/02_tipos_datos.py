from src.shared import cprint

print('Tipos de datos en python:')
print('- Numéricos: int, float, complex')
v_int = 20
cprint(v_int)

v_float = 3.14
cprint(v_float)

v_complex = 2 + 5j
cprint(v_complex)

print('\n- Texto: str')
v_str = 'Hello World'
cprint(v_str)

print('\n- Booleanos: bool')
v_bool = True
cprint(v_bool)

print('\n- Secuencias: list, tuple, range')
v_list = ["apple", "banana", "cherry"]
cprint(v_list)

v_tuple = ("apple", "banana", "cherry")
cprint(v_tuple)

v_range = range(6)
cprint(v_range)

print('\n- Mapeo: dict (llave, valor)')
v_dict = {"name": "John", "age": 36}
cprint(v_dict)

print('\n- Conjuntos: set')
v_set = {"apple", "banana", "cherry"}
cprint(v_set)
