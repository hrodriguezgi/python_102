from shared.figuras import Figuras

figura1 = Figuras('TriangULO')
area_figura1 = figura1.calcular_area(base=10, altura=4)
print(f'El área de la figura 1 es {area_figura1}')

figura2 = Figuras('Circulo')
area_figura2 = figura2.calcular_area(radio=3, altura=4)
print(f'El área de la figura 1 es {area_figura2}')
