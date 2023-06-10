import datetime
from typing import Any

class MyClass:
    genero = 'masculino'

    def __init__(self, nombre='pedro', edad=10):
        self.nombre = nombre
        self.edad = edad
        self.__grado = 8

    def saludo(self, apellido):
        print(f'Hola {self.nombre} {apellido}')
    
    def edad(self):
        print(f'{self.nombre} tiene {self.edad} años')

    @classmethod
    def cambiar_genero(cls, nuevo_genero):
        cls.genero = nuevo_genero

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self) -> str:
        return f'MyClass - {self.nombre} - {self.edad}'

    def __str__(self) -> str:
        return f'Instancia de MyClass - {self.nombre} - {self.edad}'
    
    def __metodo_privado(self):
        print('Adios Mundo cruel')

    def despedida(self):
        self.__metodo_privado()

    def __getattribute__(self, __name: str) -> Any:
        return __name

    def __setattr__(self, __name: str, __value: Any) -> None:
        __name = __value



estudiante = MyClass('andres', 20)
profesor = MyClass('carlos', 45)
generico = MyClass()

estudiante.saludo('alvarez') # -> MyClass.saludo(estudiante)
MyClass.saludo(profesor, 'aguirre')

print(estudiante.genero)

profesor.cambiar_genero('femenino')

print(generico.genero)

hoy = datetime.datetime.now()
dia_laboral = profesor.is_workday(hoy) # -> MyClass.is_workday(profesor, hoy)
print(dia_laboral)


print(estudiante) # imprime el __str__ -> usuario final
print(profesor.__repr__()) # -> desarrollador


profesor.despedida()
generico._MyClass__metodo_privado()
print('Antes de modificar', estudiante._MyClass__grado)
estudiante._MyClass__grado = 9
print('Despues de modificar', estudiante._MyClass__grado)
print('Otra instancia', generico._MyClass__grado)