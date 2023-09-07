# Funciones

Las funciones están principalmente diseñadas para evitar el repetir código en
nuestros script.

En python podemos encontrar dos tipos de funciones:
- Standard Library Functions (built-in): funciones que se encuentran en el core
de Python y pueden ser utilizadas
- Used-defined Functions: funciones que son creadas por nosotros en base a los
requerimientos que tenemos.
- Anonymous Functions: también conocidas como funciones **lambda**

## Standard Library Functions

`print()` por ejemplo es una función que se ha venido manejando a lo largo de
las sesiones.

Ejemplo:

```python
>>> print('Hola Mundo')
Hola Mundo
```

Como se observa en el ejemplo, `print` recibe unos argumentos que son requeridos
para realizar una tarea, en este caso solo le estamos enviando un string **Hola
Mundo**, y la función imprime este mismo contenido. Sin embargo print cuenta con
otros parámetros como se puede ver a continuación:

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


## User-defined Functions
La forma en como debemos declarar las funciones será con la palabra reservada
`def` de la siguiente forma:

```python
def mi_funcion():
    print('Hola Mundo')
```

La función anterior llamada `mi_funcion` ejecuta una sentencia que en este caso
es una impresión de la frase **Hola Mundo**. Declarar una función no implica que
ya se está ejecutando, para esto debemos llamarla, y para esto lo podemos hacer
de la siguiente forma:

```python
>>> mi_funcion()
Hola Mundo
```

### Documentación

La documentación o los docstrings

```python
def function_name(parameters):
    """
    Qué hace la función
    Cuáles son los parámetros
    Cuál es el retorno
    Información extra
    """
    pass
```

Con ayuda de `help` podemos ver esta documentación:

```python
>>> help(function_name)
Help on function function_name in module __main__:

function_name(parameters)
    Qué hace la función
    Cuáles son los parámetros
    Cuál es el retorno
    Información extra
```

### DRY: No repetir el código

Una de las grandes razones por las cuales se crean funciones es para evitar el
repetir el código innecesariamente, y también porque permite obtener un mejor
control del funcionamiento de nustro programa.

### Principio de Responsabilidad Única

Aunque suene repetitivo, uno de los principios en el buen diseño de funciones,
es que ellas solo se ocupen de realizar una única acción: Principio de
Responsabilidad Única. Esto también nos permite realizar un mejor debug en el
momento que se nos presente un problema.

### Elementos de las funciones

#### Parámetros
Los parámetros de las funciones son aquellos valores que pueden ser enviados
para que se realice algún tipo de sentencia al interior de la función. Un ejemplo
de esto sería una función de suma donde reciba dos operadores:

```python
def suma(op1, op2):
    print(op1 + op2)
```

De esta forma al llamar la función podemos tener el siguiente resultado:

```python
>>> suma(1, 2)
3
```

Estos parámetros pueden tener valores por defecto, para cuando el usuario no los
envíe la función pueda ejecutarse:

```python
def suma(op1 = 2, op2 = 3):
    print(op1 + op2)
```

Si llamo la función sin ningún argumento, la función sumará los valores de 2 y 3
pero si le envío valores, la función tomará estos nuevos que yo le mande:

```python
>>> suma()
5
>>> suma(4)
7
>>> suma(5,5)
10
```

#### Retorno
No siempre deseamos que la función imprima en pantalla el resultado de las
sentencias que se encuentran en ella, si no que deseamos poder almacenar el
resultado el cual puede ser un elemento o varios elementos. Para poder realizar
esto utilizaremos la sentencia `return` al interior de nuestra función de la
siguiente forma:

```python
def suma(op1 = 2, op2 = 3):
    return op1 + op2
```

De esta forma podemos almacenar el resultado de la función en otra variable de
la siguiente forma:

```python
>>> c = suma(10, 15)
>>> print(c)
25
```

Si nuestra función realiza multiples sentencias y requerimos retornar esos
objetos al exterior, bastará con enumerarlos en el `return` de la siguiente
forma:

```python
def operaciones(op1 = 10, op2 = 5):
    suma = op1 + op2
    resta = op1 - op2
    mult = op1 * op2
    div = op1 / op2
    return suma, resta, mult, div
```

Esta función retornará 4 objetos (numéricos) en una tupla, por lo que tendremos
2 alternativas para asociar esos valores:

- Alternativa 1:

```python
>>> c = operaciones()
>>> print(c)
(15, 5, 50, 2.0)
```
La variable c será una tupla que contiene los valores enviados por el `return`.

### Alternativa 2:

```python
>>> a,b,c,d = operaciones()
>>> print(a)
15
>>> print(b)
5
```

Dado que el `return` genera 4 valores, puedo asociarlos directamente al mismo
número de variables

```python
>>> a, *b = operaciones()
>>> print(a)
15
>>> print(b)
[5, 50, 2.0]
```

En este segundo ejemplo, el uso de `*` ha sido para almacenar multiples valores
en la variable `b` (el resultado de la resta, multiplicación y división). Esto
se conoce como desempaquetado de un iterable.



Asi como en otros lenguajes, Python nos da la facilidad de crear funciones que
permiten encapsular bloques de código para evitar el repetir una y otra vez las
mismas lineas para desarrollar una tarea. 

Un ejemplo podría ser el siguiente: *La siguiente lista nos presenta 5 diferentes
tuplas con el ancho y largo de diferentes recangulos. Diseñe un algoritmo que
nos permita identificar el área de cada uno de ellos*.

La lista de las medidas de los rectangulos es la siguiente:

```python
dimensiones = [(2,4), (3,5), (3,6), (2,5), (4,7)]
```

Una alternativa para realizar esto podría ser:

```python
>>> area_1 = dimensiones[0][0] * dimensiones[0][1]
>>> area_2 = dimensiones[1][0] * dimensiones[1][1]
>>> area_3 = dimensiones[2][0] * dimensiones[2][1]
>>> area_4 = dimensiones[3][0] * dimensiones[3][1]
>>> area_5 = dimensiones[4][0] * dimensiones[4][1]
>>> print(area_1, area_2, area_3, area_4, area_5)
8 15 18 10 28
```

Si revisamos bien el código, la acción fue la misma, multiplicar ambos valores
de las tuplas que se encuentran en la lista. Acá es donde viene la ventaja de
utilizar funciones, poder encapsular el fragmento de código que se repite
constantemente para ser más eficientes. Una posible solución entonces sería:

```python
>>> def area(largo:int, ancho:int) -> int:
>>>     return largo * ancho
>>> 
>>> areas = []
>>> for dimension in dimensiones:
>>>     areas.append(area(dimension[0], dimension[1]))
>>> 
>>> print(areas)
[8, 15, 18, 10, 28]
```