"""
Vamos a crear una clase llamada 'Circulo', que debe tener como métodos:
1. área del Circulo
    area = pi * radio^2
2. perímetro del Circulo.
    perimetro = 2 * pi * radio

Desarrollo:

Atributo: radio
Constante: pi, 2
"""

from math import pi, pow


class Circulo:
    """
    Class example
    """
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return pi * pow(self.radio, 2)

    def perimetro(self):
        return 2 * pi * self.radio


class Rectangulo:
    """
    Class example
    """
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho

    def perimetro(self):
        return 2 * (self.largo + self.ancho)
