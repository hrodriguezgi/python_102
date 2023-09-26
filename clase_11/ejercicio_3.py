# PEP8 -> Estándar
# Librerías built-in (estándar)
# Librerías de terceros
# Librerías propias

# variables -> minusculas
# funciones -> snake case
# clases -> camel case
# constantes -> mayusculas

import os
import datetime
import json

import matplotlib
import pandas
import numpy

from libraries.figuras import Figuras
from libraries.figuras import Person


figura1 = Figuras('TRIANGULO')
area_figura1 = figura1.calcular_area(base=10, altura=4)
print(f'El área de la figura 1 ({figura1.nombre_figura}) es {area_figura1}')
figura1.calcular_perimetro()

figura2 = Figuras('Circulo')
area_figura2 = figura2.calcular_area(radio=3)
print(f'El área de la figura 2 ({figura2.nombre_figura}) es {area_figura2}')
figura2.calcular_perimetro()

persona = Person()
