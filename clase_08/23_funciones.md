# Funciones

Las funciones están principalmente diseñadas para evitar el repetir código en
nuestros script y ser más eficientes en el desarrollo.

En python podemos encontrar tres tipos de funciones:
- Standard Library Functions (built-in): funciones que se encuentran en el core
de Python y pueden ser utilizadas
- Anonymous Functions: también conocidas como funciones **lambda**
- Used-defined Functions: funciones que son creadas por nosotros en base a los
requerimientos que tenemos.

## Standard Library Functions

### `print()` 

La función `print()` permite imprimir en pantalla (**sys.stdout**) un objeto.
Ejemplo:

```python
>>> print('Hola Mundo')
Hola Mundo
```

Como se observa en el ejemplo, `print` recibe unos argumentos que son requeridos
para realizar una tarea, en este caso solo le estamos enviando un string ***Hola
Mundo***, y la función imprime este mismo contenido. Sin embargo `print` cuenta
con otros parámetros como se puede ver a continuación:

```python
print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
```

Si hacemos uso de otros argumentos podemos ver como el comportamiento de la
función `print` puede variar:

```python
>>> str1 = 'Hola Mundo'
>>> str2 = 'Cruel'
>>> print(str1, str2, sep='*-*', end='')
Hola Mundo*-*Cruel
```

### `isinstance()`

```python
isinstance(obj, class_or_tuple, /)
    Return whether an object is an instance of a class or of a subclass thereof.
    
    A tuple, as in ``isinstance(x, (A, B, ...))``, may be given as the target to
    check against. This is equivalent to ``isinstance(x, A) or isinstance(x, B)
    or ...`` etc.
```

La función `isinstance()` nos permite evaluar si un objeto pertenece a una tipo
de objeto, retornando un valor de `True` cuando si lo es, o `False` en otro caso.
Ejemplo:

```python
>>> numeros = [1,2,3,4]
>>> isinstance(numeros, list)
True
>>> isinstance(numeros, dict)
False
```

### `zip()`

```python
zip(object)
    zip(*iterables) --> A zip object yielding tuples until an input is exhausted.
    
       >>> list(zip('abcdefg', range(3), range(4)))
       [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]
    
    The zip object yields n-length tuples, where n is the number of iterables
    passed as positional arguments to zip().  The i-th element in every tuple
    comes from the i-th iterable argument to zip().  This continues until the
    shortest argument is exhausted.
```

La función `zip(*iterables)` genera un nuevo elemento iterable de tuplas, donde
cada tupla corresponde a un elemento de cada uno de los iterables de entrada. La
longitud final del iterable resultado dependerá de la longitud mínima de los
elementos de entrada. Ejemplo:

```python
>>> numeros = [1, 2, 3, 4, 5]
>>> vocales = ['a', 'e', 'i', 'o', 'u']
>>> zip(numeros, vocales)
<zip at 0x7fa2f0776b40>
>>> list(zip(numeros, vocales))
[(1, 'a'), (2, 'e'), (3, 'i'), (4, 'o'), (5, 'u')]
>>> numeros.append(6)
>>> numeros
[1, 2, 3, 4, 5, 6]
>>> list(zip(numeros, vocales))
>>> [(1, 'a'), (2, 'e'), (3, 'i'), (4, 'o'), (5, 'u')]
```

La función `zip` en conjunto con el operador `*` de desempaquetar, permite tomar
un iterable y retornar dos o mas diferentes secuencias:

```python
>>> secuencia = [(1,'a','a'), (2,'e','v'), (3,'i','i'), (4,'o','o'), (5,'u','n')]
>>> num, voc, pal = zip(*secuencia)
>>> num
(1, 2, 3, 4, 5)
>>> voc
('a', 'e', 'i', 'o', 'u')
>>> pal
('a', 'v', 'i', 'o', 'n')
```

### `map()`

```python
map(object)
    map(func, *iterables) --> map object
    
    Make an iterator that computes the function using arguments from
    each of the iterables.  Stops when the shortest iterable is exhausted.
```

La función `map()` es utilizada para aplicar una función a cada uno de los
elementos de un iterable. El objeto resultande es de tipo `map`, el cual es un
iterador que puede ser convertido en lista con la función de `list()`. Esta
función toma como primer argumento la función (que puede ser las propias de
Python o una creada por el usuario), y como segundo argumento un iterable.
Ejemplo:

```python
>>> vocales = ['a', 'e', 'i', 'o', 'u']
>>> VOCALES = list(map(str.upper, vocales))
>>> print(VOCALES)
['A', 'E', 'I', 'O', 'U']
```

Otro ejemplo:

```python
>>> from math import sqrt
>>> numeros = [1, 4, 9, 16, 25]
>>> raices = list(map(sqrt, numeros))
>>> print(raices)
[1.0, 2.0, 3.0, 4.0, 5.0]
```

### `filter()`

```python
filter(object)
    filter(function or None, iterable) --> filter object
    
    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
```

La función `filter()` toma una función y un iterable como argumentos, y retorna
los elementos del iterable para los cuales la función sea verdadero. Esta función
al igual que `map` acepta funciones propias, anónimas y definidas por el usuario.
Ejemplo:

```python
>>> numeros = [1, 4, 9, 16, 25]
>>> pares = list(filter(lambda x: x%2==0, numeros))
>>> print(pares)
[4, 16]
```

### `input()`

```python
input(prompt=None, /)
    Read a string from standard input.  The trailing newline is stripped.
    
    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.
    
    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.
```

La función `input()` toma la entrada de un usuario, retornandolo como cadena.
Esta función toma un argumento opcioinal (prompt) el cual es un mensaje que
puede ser mostrado al usuario a quien se le pide una entrada. Ejemplo

```python
>>> nombre = input('Ingrese su nombre: ')
Ingrese su nombre: Harvey

>>> print(nombre)
Harvey
```

Si se requiere capturar el valor capturado como numérico, se deberá realizar el
correspondiente casteo, como se muestra en el siguiente ejemplo:

```python
>>> edad = int(input('Ingrese su edad: '))
Ingrese su edad: 25

>>> print(edad)
25
```

### `id()`

```python
id(obj, /)
    Return the identity of an object.
    
    This is guaranteed to be unique among simultaneously existing objects.
    (CPython uses the object's memory address.)
```

La función `id()` retorna la identidad de un objeto. Esto es un valor numérico
el cual es único y constante para el objeto durante su ciclo de vida. Ejemplo:

```python
>>> numeros = [1, 4, 9, 16, 25]
>>> numeros_2 = numeros
>>> print(f'Id numeros: {id(numeros)}')
Id numeros: 140337929437824
>>> print(f'Id numeros_2: {id(numeros_2)}')
Id numeros_2: 140337929437824
```

## Funciones Lambda

Las funciones lambda, también conocidas como anónimas, debido a que son definidas
sin nombre. Las funciones lambda son definidas de la siguiente forma:

```python
lambda parámetros: acción
```

Las características de este tipo de funciones son las siguientes:
- Son funciones que pueden definir cualquier número de parámetros pero una única
expresión. Esta expresión es evaluada y devuelta.
- Se pueden usar en cualquier lugar en el que una función sea requerida.
- Estas funciones están restringidas al uso de una sola expresión.
- Se suelen usar en combinación con otras funciones, generalmente como argumentos
de otra función.

Ejemplo:

```python
>>> resultado = lambda x, y: x * y
>>> print(resultado(10,25))
250
```

Este tipo de funciones, son comunmente utilizadas en combinación de `map()`,
`filter()` y `reduce()`.

### `map()`

```python
>>> numeros = [1, 4, 9, 16, 25]
>>> cuadrados = list(map(lambda x: x ** 2, numeros))
>>> print(cuadrados)
[1, 16, 81, 256, 625]
```

Un uso interesante de las funciones lambda, es que se puede pasar una lista de
funciones como segundo argumento:

```python
>>> numeros = [1, 4, 9, 16, 25]
>>> cuadrado = lambda x: x ** 2
>>> cubo = lambda x: x ** 3
>>> funciones = [cuadrado, cubo]
>>> valores = [ list(map(lambda x: x(num), funciones)) for num in numeros ]
>>> print(valores)
[[1, 1], [16, 64], [81, 729], [256, 4096], [625, 15625]]
```

### `filter()`

```python
>>> numeros = [1, 4, 9, 16, 25]
>>> pares = list(filter(lambda x: x%2==0, numeros))
>>> print(pares)
[4, 16]
```

### `reduce()`

Esta función realiza un calculo acumulativo sobre una lista y retorna el valor
resultante. Esta función está incluida en el módulo `functools`.

```python
>>> from functools import reduce
>>> numeros = [1, 4, 9, 16, 25]
>>> suma = reduce(lambda x, y: x + y, numeros)
print(suma)
21
```