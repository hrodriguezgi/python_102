"""control = 0

while True:
    print('ciclo infinito', control)
    if control == 1000000:
        break
    control += 1
"""

"""
j = 10
while True:
    if j < 5:
        break
    print(j)
    j -= 1
"""

"""
for i in range(10): # --> 0 1 2 3 4 5 6 7 8 9
    if i == 5:
        break
    print(i)
"""

"""
for i in range(10): # --> 0 1 2 3 4 5 6 7 8 9
    if i == 5:
        continue
    print(i)
"""

"""
for i in range(10): # --> 0 1 2 3 4 5 6 7 8 9
    if i == 5:
        pass
    print(i)
"""

def impresion_hola():
    # TODO: definir las condiciones de calculo interés
    pass

for i in str('Hola Mundo'):
    if i.upper() == 'O':
        print('O encontrada')
        break
    print(i)