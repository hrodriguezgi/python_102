"""
# if
n = 4
if (n % 2 == 0 or n > 5) and (n % 4 == 1 or n < 5):
    print('n es un número par')



# if - else
n = 14
if n % 2 == 0:
    print('n es un número par')
else:
    print('n es un número impar')

# Lo anterior en operador ternario
# print('n es un número par') if n % 2 == 0 else print('n es un número impar')

print('lo demás')
"""


# if anidado
a = 15
b = 10
c = 15
if a > b:
    if a > c:
        print('a es el más grande de todos')
    elif a == c:
        print('a y c son iguales')
    else:
        print('esta es la respuesta')
        print('c es el más grande de todos')
elif b > c:
    print('b es el más grande de todos')
else:
    print('c es el más grande de todos')






"""
# if - elif - else
a = 5
b = 10
if a == b:
    print('Los números son iguales')
elif a > b:
    print('a es mayor que b')
elif b % a == 0:
    b = b**2
    print('b es divisible por a')
    print(b)
    print(a*b, 'otro texto')
else:
    print('b es mayor que a')
"""