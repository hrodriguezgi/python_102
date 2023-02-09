# Operadores


print('Operadores Aritméticos')
a = 9
b = 4
print(f'  a: {a}')
print(f'  b: {b}')
print()

print(f'  a + b: {a + b}')
print(f'  a - b: {a - b}')
print(f'  a * b: {a * b}')
print(f'  a / b: {a / b}')
print(f'  a // b: {a // b}')
print(f'  a % b: {a % b}')
print(f'  a ** b: {a ** b}')
print('\n')


print('Operadores de Comparación')
a = 13
b = 33
print(f'  a: {a}')
print(f'  b: {b}')
print()

print(f'  a > b: {a > b}')
print(f'  a < b: {a < b}')
print(f'  a == b: {a == b}')
print(f'  a != b: {a != b}')
print(f'  a >= b: {a >= b}')
print(f'  a <= b: {a <= b}')
print('\n')


print('Operadores Lógicos')
a = True
b = False
print(f'  a: {a}')
print(f'  b: {b}')
  
print(f'  a and b: {a and b}')
print(f'  a or b: {a or b}')
print(f'  not a: {not a}')
print('\n')


print(f'Operadores Bit a Bit')
a = 10
b = 4
print(f'  a: {a}')
print(f'  b: {b}')
print()

print(f'  a & b: {a & b}')
print(f'  a | b: {a | b}')
print(f'  ~a: {~a}')
print('\n')


print('Operadores de Asignación')
a = 10
b = a
print(f'  a: {a}')
print(f'  b: {b}')
print()

print(f'  b = a: {b}')
b += a
print(f'  b += a: {b}')
b -= a
print(f'  b -= a: {b}')
b *= a
print(f'  b *= a: {b}')
print('\n')


print('Operadores de Identidad')
a = 10
b = a
c = 10
print(f'  a: {a}')
print(f'  b: {b}')
print(f'  c: {c}')
print()

print(f'  b is a: {b is a}')
print(f'  c is not a: {c is not a}')
print('\n')


print('Operadores de Pertenencia')
a = 10
b = [num*2 for num in range(6)]
c = [num*3 for num in range(6)]
print(f'  a: {a}')
print(f'  b: {b}')
print(f'  c: {c}')
print()

print(f'  a in b: {a in b}')
print(f'  a not in c: {a not in c}')
print('\n')

print('Operadores Ternarios')
a = 10
b = 5
print(f'  a: {a}')
print(f'  b: {b}')
print()

print(f'  if a > b then "a" else "b": {a if a > b else b}')
print(f'  if a % b == 0 then "divisible" else "no divisible": {"divisible" if a % b == 0 else "no divisible"}')
print('\n')
