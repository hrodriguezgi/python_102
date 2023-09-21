"""
Area y Perímetro de las figuras geométricas
- Rectángulo:
    - Area: l1 x l2
    - Perímetro: 2 x l1 + 2 x l2
- Circulo:
    - Area: pi x r^2
    - Perímetro: 2 x pi x r
- Triangulo:
    - Área: (base x altura)/2
    - Perímetro: l1 + l2 + l3
"""

from math import pi


class Figuras:
    def __init__(self, figura: str) -> None:
        self.nombre_figura = figura.lower()
        self.area = 0
        self.perimetro = 0
        self.pi = pi

    def calcular_area(self, **kwargs) -> float:
        if self.nombre_figura == 'circulo':
            if 'radio' in list(kwargs.keys()):
                self.area = self.pi * kwargs['radio'] ** 2
        elif self.nombre_figura == 'triangulo':
            if 'base' in list(kwargs.keys()) and 'altura' in list(kwargs.keys()):
                self.area = (kwargs['base'] * kwargs['altura'])/2
        elif self.nombre_figura == 'rectangulo':
            if 'lado_1' in list(kwargs.keys()) and 'lado_2' in list(kwargs.keys()):
                self.area = kwargs['lado_1'] * kwargs['lado_2']
        return self.area

    def calcular_perimetro(self):
        pass
