from shared.figuras import Circulo


radio = input('Digite el radio: ')
circulo_1 = Circulo(float(radio))
# Imprimimos el radio del circulo_1
print(circulo_1.radio)
# Imprimimos el área del circulo_1
print(circulo_1.area())
# Imprimimos el perímetro del circulo_1
print(circulo_1.perimetro())
