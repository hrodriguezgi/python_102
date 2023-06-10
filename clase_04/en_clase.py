n = 4
if n % 2 == 0:
    print(f'{n} es un número par')
else:
    print('no se cumple la condición')

# En operador ternario la sentencia anterior es:
n = 5
print(f'{n} es un número impar') if n % 2 == 1 else print('no se cumple la condición')


# if - elif

a = 5*2
b = 10
if a == b:
    print('Los números son iguales')
elif a > b:
    print('a es mayor que b')
else:
    print('b es mayor que a')

# if anidado

a = 5
b = 15
c = 15
if a > b:
    if a > c:
        print('a es el más grande de todos')
    else:
        print('c es el más grande de todos')
elif b > c:
    print('b es el más grande de todos')
elif b == c:
    print('b es igual a c')
else:
    print('c es el más grande de todos')


# For

numeros = [1, 2, 3]
letras = ['a','b','c']
for numero in numeros:
    print(f'el cuadrado de {numero} es {numero**2}')
    for letra in letras:
        print(f'\tla letra es: {letra}')


# while

a = 5
b = 0
while b < a:
    print(f'el valor de a es: {a}')
    a -= 1
