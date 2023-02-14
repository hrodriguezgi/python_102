# Control de decisiones
El control de deciciones también es conocido como selección de sentencias o
ramificaciones de sentencias. Estas pueden realizarse con ayuda de condicionales

Los controles de decisión son por lo tanto:

## if
Las sentencias if son utilizadas para el control de flujo que nos ayudan a
ejecutar cierta parte del código siempre y cuando se cumpla la condición que se
ha definido.


Ejemplo:

```python
n = 10
if n % 2 == 0:
    print('n es un número par')
```


## if - else
Las sentencias if - else son un complemento de las anteriores, ya que nos
permiten definir dos caminos: cuando se cumple la condición y cuando no se
cumple la condición, teniendo la oportunidad de definir de segmentos de código
para cada uno de los escenarios.


Ejemplo:

```python
n = 13
if n % 2 == 0:
    print('n es un número par')
else:
    print('n es un número impar')
```

**Nota:**

No olvidar que este tipo de sentencias también pueden ser escritas como operador
ternario


## if anidado
Las sentencias con un if anidado, no son más que definir un if dentro de otro
if y cumpliendo las reglas de los puntos 1 y 2.


Ejemplo:

```python
a = 5
b = 10
c = 15
if a > b:
    if a > c:
        print('a es el más grande de todos')
    else:
        print('c es el más grande de todos')
elif b > c:
    print('b es el más grande de todos')
else:
    print('c es el más grande de todos')
```


## if - elif - else
Las sentencias con if - elif - else nos permiten adicionarle una condición más
a los simples if - else, teniendo la posibilidad de 3 caminos para nuestra
toma de decisión.


Ejemplo:

```python
a = 5
b = 10
if a == b:
    print('Los números son iguales')
elif a > b:
    print('a es mayor que b')
else:
    print('b es mayor que a')
```
