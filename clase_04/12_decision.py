"""
# if
n = 4
if (n % 2 == 0 or n > 5) and (n % 4 == 1 or n < 5):
    m = n ** 4
    print(f'el valor de m es {m}')
    print('n es un número par')
"""

"""
# Operadores ternarios
# on_true if expression else on_false
n = 258
m = "Cumple" if (n % 2 == 0 or n > 5) else "No cumple"
print(m)

n = 3
m = "Cumple" if (n % 2 == 0 or n > 5) else ("cumple b" if n == 4 else "no cumple b")

En if-else:
n = 3
if (n % 2 == 0 or n > 5):
    m = "Cumple"
else:
    if n == 4:
        m = "cumple b"
    else:
        m = "no cumple b"

print(m)
"""

"""
# if - else
n = 14
if n % 2 == 0:
    print("n es un número par")
else:
    print("n es un número impar")

    # Lo anterior en operador ternario
    # print('n es un número par') if n % 2 == 0 else print('n es un número impar')

print("lo demás")
"""

"""
# if anidado
a = 9
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
    print("Los números son iguales")
elif a > b:
    print("a es mayor que b")
elif b % a == 0:
    b = b**2
    print("b es divisible por a")
    print(b)
    print(a * b, "otro texto")
else:
    print("b es mayor que a")
