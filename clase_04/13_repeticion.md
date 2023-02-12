# Repeticiones

Las sentencias de repetición, también conocidas como ciclos, son utilizadas para
repetir bloques de código.

En Python podemos encontrar dos sentencias de ciclos:
1. for loop
2. while loop


## for loop
Esta sentencia es utilizada para iterar sobre una secuencia (lista, tupla,
diccionario, conjunto, range). El objetivo es ejecutar una sentencia para cada
uno de los elementos de la secuencia.

- Ejemplo:
```python
lista = [1, 2, 3, 4, 5]
for i in lista:
    print(f'el cuadrado de {i} es {i**2}')
```

## while loop
Esta sentencia es utilizada para ejecutar un bloque de código hasta que una
condición dada se cumpla. Esto quiere decir que esta condición es validada cada
vez que se itera sobre el ciclo.

- Ejemplo:
```python
a = 5
b = 0
while b < a:
    print(f'el valor de b es: {b}')
    b +=1
```