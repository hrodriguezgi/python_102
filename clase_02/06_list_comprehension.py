print(f'''
Para crear dinámicamente una lista, se puede hacer por medio de ciclos: 'for'
Un ejemplo de esto es el siguiente código, que se encarga de almacenar los
números del 1 al 10 en una lista llamada 'numeros', sin embargo es necesario
tener en cuenta que se debe inicializar la lista antes de ejecutar el ciclo''')

numeros = []
for numero in range(1, 11):
  numeros.append(numero)

print(f'''
numeros = []
for numero in range(1, 11):
    numeros.append(numero)

El resultado es el siguiente:
- numeros: {numeros}
''')

print(f'''
Por otro lado, tenemos la alternativa de crear la lista haciendo uso de list
comprehension, el cual resume las 3 anteriores lineas de código en una sola, de
la siguiente forma:

numeros_2 = [numero for numero in range(11, 21)]
''')

numeros_2 = [numero for numero in range(11, 21)]

print(f'''
El resultado de ese código es el siguiente:
- numeros_2: {numeros_2}
''')

print(f'''
Por último, las list comprehension también admiten condicionales en su
ejecución. El código ejemplo es el siguiente:

numeros_3 = [numero for numero in range(21, 31) if numero % 2 == 0]
''')

numeros_3 = [numero for numero in range(21, 31) if numero % 2 == 0]

print(f'''
El resultado es el siguiente:
- numeros_3: {numeros_3}
''')