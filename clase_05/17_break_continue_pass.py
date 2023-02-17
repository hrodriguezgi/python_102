# break
print('Uso del break en ciclo for:\n')
for i in range(10):
    print(i)
    if i == 5:
        break

print('\n\nUso del break en ciclo while:\n')
j = 10
while True:
    print(j)
    if j < 5:
        break
    j -= 1


# continue
print(f'\n{50*"-"}')
print('\n\nUso del continue en ciclos:\n')
for i in range(10):
    if i == 5:
        continue
    print(i)


# pass
print(f'\n{50*"-"}')
print('\n\nUso del pass en ciclos:\n')
for i in str('Hola Mundo'):
    if i.upper() == 'O':
        print('O encontrada')
        pass
    print(i)