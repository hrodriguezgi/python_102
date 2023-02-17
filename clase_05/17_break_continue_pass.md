# Control de Ciclos

## `break`
Esta sentencia es utilizada para terminar por lo general un ciclo o donde se
esté utilizando. Después del `break`, el código continuará con las sentencias
que se encuentren posterior a él. Si este se encuentra en un ciclo (o ciclo
anidado) la siguiente sentencia será la que procede después del ciclo.

Ejemplos:

- `for`

```python
for i in range(10):
    print(i)
    if i == 5:
        break
```


- `while`

```python
j = 10
while True:
    print(j)
    if j < 5:
        break
    j -= 1
```

## `continue`
Esta es una sentencia de control similar a `break` utilizada en los ciclos, sin
embargo es todo lo opuesto a ella, ya que `continue` en lugar de detener el
ciclo, obliga a que se realice la siguiente iteracion, sin que se realice el
código que se encuentra debajo de la sentencia.

Ejemplo:

```python
for i in range(10):
    if i == 5:
        continue
    print(i)
```


## `pass`
Esta sentencia es utilizada para no hacer nada. En python es utilizado en
ocasiones cuando debido a la sintaxis se requiere algún comando pero no se
cuenta con ello.

Ejemplo:

```python
def mi_funcion():
    pass
```

```python
for i in str('Hola Mundo'):
    if i.upper() == 'O':
        print('O encontrada')
        pass
    print(i)
```