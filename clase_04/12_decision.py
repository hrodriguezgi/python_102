# if
n = 10
if n % 2 == 0:
    print('n es un número par')


# if - else
n = 13
if n % 2 == 0:
    print('n es un número par')
else:
    print('n es un número impar')


# if anidado
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


# if - elif - else
a = 5
b = 10
if a == b:
    print('Los números son iguales')
elif a > b:
    print('a es mayor que b')
else:
    print('b es mayor que a')