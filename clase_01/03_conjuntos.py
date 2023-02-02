# Conjuntos (sets)

print(f'''
Conjuntos
---------
Los conjuntos son un tipo de dato en python que se conocen por ser iterables
como lo son las listas y las tuplas, pero con una condición especial: no 
permiten elementos duplicados, y no son ordenados. Adicional, se pueden
realizar las operaciones entre conjuntos vistas en el colegio: union,
intereseccion, diferencia y una nueva: diferencia simétrica\n''')

# Creamos varios conjuntos
set_pares = {2, 4, 6, 8, 10}
set_impares = {1, 3, 5, 7, 9}
set_primos = {1, 2, 3, 5, 7}

print(f'''Los conjuntos creados son:
- set_pares: {set_pares}
- set_impares: {set_impares}
- set_primos: {set_primos}
''')

set_vocales = {'a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u'}

print(f'''Conjunto con elementos duplicados: {set_vocales}''')

print(f'''
Operaciones entre conjuntos
---------------------------
Unión: puede realizarse de dos formas: set_1.union(set_2) ó set_1 | set_2
 Ejemplos:
    - set_pares.union(set_impares) = {set_pares.union(set_impares)}
    - set_pares | set_primos = {set_pares | set_primos}

Interseccion: puede realizarse de dos formas: set_1.intersection(set_2) 
 ó set_1 & set_2
 Ejemplos:
    - set_primos.intersection(set_impares) = {set_primos.intersection(set_impares)}
    - set_pares & set_primos = {set_pares & set_primos}

Diferencia: puede realizarse de dos formas: set_1.difference(set_2)
 ó set_1 - set_2
 Ejemplos:
    - set_impares.difference(set_primos) = {set_impares.difference(set_primos)}
    - set_pares - set_primos = {set_pares - set_primos}

Diferencia Simétrica: puede realizarse de dos formas: 
 set_1.symmetric_difference(set_2) ó set_1 ^ set_2
 Ejemplos:
    - set_impares.symmetric_difference(set_primos) = {set_impares.symmetric_difference(set_primos)}
    - set_pares ^ set_primos = {set_pares ^ set_primos}
''')