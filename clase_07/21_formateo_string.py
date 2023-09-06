## Formateo utilizando `%`
print(f"{5*'*'} Formateo utilizando % {5*'*'}\n")

print('Ejemplo 1:')
x = 'con'
print("Camilo %s futbol %s sus amigos"%('juega',x))


print('\nEjemplo 2:')
print('%s tiene %d perros' %('Carlos', 4))

print('\nEjemplo 3:')
print('El valor de PI es de %f' %(3.141593))


print(f'\n{40*"-"}\n')
## Formateo utilizando el metodo `format()`
print(f"{5*'*'} Formateo utilizando el metodo format() {5*'*'}\n")

print('Ejemplo 1:')
print('{} tiene {} perros'.format('Carlos', 4))


### Inserción de datos por posición:
print('\nEjemplo 2:')
print('{1} tiene {0} perros'.format(4, 'Carlos'))


### Inserción de datos por llaves (permite también el reuso):
print('\nEjemplo 3:')
print('{nombre} tiene {valor} perros'.format(nombre='Carlos', valor=4))


print(f'\n{40*"-"}\n')
## Formateo utilizando los `F-strings`
print(f"{5*'*'} Formateo utilizando los F-strings {5*'*'}\n")

print('Ejemplo 1:')
nombre='CARLOS'
valor=4
print(f'{nombre.title()} tiene {valor} perros')



print(f'\n{40*"-"}\n')
# Formateo de números
print(f"{5*'*'} Formateo de números {5*'*'}\n")

print('Ejemplo 1:')
figura:str = 'circulo'
area:str = '2 x pi x r^2'
print(f'El area del {figura} es igual a {area}')

print('\nEjemplo 2:')
radio:float = 3.14
from math import pi
print(f'El area del {figura} de radio = {radio} es de {2*pi*(radio**2):.3f}')

print(f'{3.15:.1f}')
print(f'{2.75:.1f}')
