# Estructuras de Control
Python es un lenguaje que tiene tres tipo de control de estructuras:
1. Secuencial
2. Selección
3. Repetición

En este caso identificaremos la primera: secuencial y de que se trata.

# Control secuencial
Como ya lo hemos visto, Python es un lenguaje interpretado, y en el control de
tipo secuencial lo vemos en su máxima expresión, ya que a medida que Python va
interpretando una a una nuestras lineas de código de forma secuencial va
realizando las acciones que le pedimos. Ejemplo:

```python
a = 20
b = 10
c = a - b
print("La resta es igual a:",c)
```

Al obversar detalladamente este fragmento de código vemos como todo sucede en
una forma secuencial.


- Ejemplo 1
```python
a = 20
b = 10
c = a - b
print("La resta es igual a:",c)
```


- Ejemplo 2:
```python
a = ['amarillo', 'rojo', 'azul']
b = ['cafe', 'morado', 'verde']
a.extend(b)
print("La unión de las dos listas da como resultado",a)
```
