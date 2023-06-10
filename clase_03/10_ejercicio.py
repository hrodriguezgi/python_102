from random import randint

"""
Ejercicio 1.

Por medio de la libreria random, podemos crear valores numéricos aleatorios, 
haciendo uso de la siguiente sintaxis:

    random.randint(1, 10)

El comando anterior generará un único valor entre 1 y 10 incluídos cada que lo 
ejecutamos.

Haciendo uso de la librería random, escribir el código necesario para:
 a. Almacene en las variables num1, num2 y num3 tres valores generados aleatoriamente
    entre el 10 y el 30.

 b. Si num1 es mayor que num2 sumado con num3, se debe imprimir el valor de num1
    en caso contrario se deberá imprimir num2

 c. Si num3 es multiplo de num2, imprimir "el num3 contiene XX veces el num2"
    en caso contrario imprimir "no son multiplos"
"""

# escribir el código aquí


"""
Ejercicio 2.
Haciendo uso de la libreria random, escribir el código necesario para:
 a. Generar una lista de 10 elementos con números aleatorios entre 5 y 15 y
    almacenarla en una variable llamada list1

 b. Generar un número aleatorio entre el 5 y el 15 y almacenarlo en una 
    variable llamada num1 

 c. Si num1 se encuentra en la list1 se debe imprimir "contenido" en caso 
    contrario se debe imprimir "no contenido"
"""

# escribir el código aquí

#list1 = list()
#for valor in range(1, 11):
#    list1.append(randint(5, 15))
list1 = [randint(5, 15) for _ in range(10)]

print(f'la longitud de la lista list1 es {len(list1)}')
print(f'los elementos de la list1 son: {list1}')
