# Parte 1
try:
    print(10 / c)
except ZeroDivisionError:
    print(f'El denominador no puede ser cero')
except TypeError:
    print(f'El denominador debe de ser de tipo numérico')
except Exception as e:
    print(f"Error inesperado: {e}")
print()

# Parte 2
try:
    with open('test.txt') as file:
        content = file.read()
except FileNotFoundError:
    print(f'El archivo no fue encontrado')
else:
    print(content)
finally:
    print("Fin del programa")

try:
    f = open('nuevo_file.txt', 'w')
except Exception as e:
    print(f'{e}')
else:
    f.write('Hola mundo cruel\n')
    f.close()