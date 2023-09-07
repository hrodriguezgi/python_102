suma = 40


# argumentos opcionales o con valores por defecto
def saludo(nombre='Carlos', ciudad='Medellin', edad=30):
    print(f'Hola {nombre}, que vive en {ciudad} y tiene {edad} años')

saludo('Andres', 'Cartagena', 25)
saludo()

print(f'{50*"-"}')

# argumentos por posición y por asignación
def dividido(op1, op2):
    print(op1 / op2)

# posición
dividido(10, 30)

# asignación
dividido(op2=10, op1=30)

# Esto genera error
# dividido(op2=20, 100)
print(f'{50*"-"}')

# argumentos obligatorios y opcionales
def dividido_2(op4, op3, op2=10, op1=20):
    print((op1 / op2)*op3)
    print(op4)

dividido_2(1000, 10)

dividido_2(1000, 10,2,3)

print(f'{50*"-"}')
print('Ejemplo 3:\n')
# argumentos variables
def muchos_argumentos(*args):
    print(type(args), args)
    for i in args:
        print(i)
    print()

muchos_argumentos(1,2)
muchos_argumentos(1,2,3)
muchos_argumentos('a')
muchos_argumentos()

print(f'{50*"-"}')
print('Ejemplo 4:\n')

def posicion_variable(a, b, *args):
    print(a, b)
    print(type(args), args)
    print()

posicion_variable(1,2)
posicion_variable(1,2,3,4,5)
posicion_variable('hola', ['a','b','c'],'mundo')


print(f'{50*"-"}')
print('Ejemplo 5:\n')
# llave-valor variables
def llave_valor(**kwargs):
    print(type(kwargs), kwargs)
    for i in kwargs.values():
        print(i)
    print()


llave_valor(a=10, b='hola')


print(f'{50*"-"}')
print('Ejemplo 6:\n')
# argumentos y llave-valor variables
def arg_llave_valor(*args, **kwargs):
    print(type(args), args)
    print(type(kwargs), kwargs)
    print()

arg_llave_valor(1,2, a=1, b=2)
arg_llave_valor(a=1, b=2)
arg_llave_valor(1,2)


print(f'{50*"-"}')
print('Ejemplo 7:\n')
def full(a, b=10, *args, **kwargs):
    print(type(a), a)
    print(type(b), b)
    print(type(args), args)
    print(type(kwargs), kwargs)
    print()

full(10)
full(10, 20)
full(10, 20, 1,2,3,4)
full(10, 20, 1,2,3,4, nombre='harvey', edad=30)



print(f'{50*"-"}')
print('Ejemplo 8:\n')
print(f'antes de la funcion: {suma}')

def suma_1(a, b=10, *args, **kwargs):
    global suma
    suma = a + b
    print(f'dentro de la funcion: {suma}')
    return a + b

resultado = suma_1(40) # Esta función retorna un valor y lo asignamos a la variable resultado
print(resultado)
print(f'despues de la funcion: {suma}')



print(f'{50*"-"}')
print('Ejemplo 9:\n')
# recursividad
def factorial(x):
    if x == 1:
        return 1 # retorna un int
    else:
        return x * factorial(x - 1) # int mul funcion?
    
fact = factorial(5)
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1

print(fact)


print(f'{50*"-"}')
print('Ejemplo 10:\n')

def suma_retorno_variable(a, b, c):
    suma1 = a + b
    suma2 = a + c
    return suma1, suma2

resultado = suma_retorno_variable(1,2,3)
print(type(resultado), resultado)

print(f'{50*"-"}')
print('Ejemplo 10:\n')

def suma_retorno_variable(a, b, c):
    lista = ['1','2']
    suma1 = a / b
    suma2 = a + c
    return suma1, suma2, lista

var_a = suma_retorno_variable(1,2,3)
print(type(var_a), var_a)

for i in var_a:
    print(type(i), i)