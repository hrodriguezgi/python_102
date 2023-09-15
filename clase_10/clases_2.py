class EmployeeEmpty:
    def __init__(self):
        self.name = 'Carlos'
        self.last = 'Aguirre'
        self.salary = 1000

class Employee:
    raise_amount = 1.04

    def __init__(self, name:str = 'Pedro', last:str = 'Navajas', salary:int = 500):
        self.name = name
        self.last = last
        self.email = name + '.' + last + '@company.com'
        self.salary = salary
        self.__edad = 30

    def saludo(self, titulo:str) -> None: # método regular con un parámetro
        print(f'Hola {titulo} {self.name}, cómo estas?')

    def despedida(self): # método regular sin parámetro
        print(f'Hasta pronto {self.name} {self.last}')

    @staticmethod # Decorador
    def despedida_generica() -> None:
        print(f'vuelva pronto')
    
    @classmethod # decorador
    def new_raise(cls, new_amount:float) -> None:
        cls.raise_amount = new_amount

    def __repr__(self) -> str:
        return f'Employee Class - {self.name} {self.last} {self.salary}' # usuario desarrollador

    def __str__(self) -> str:
        return f'Employee Class - {self.name} {self.last}' #usuario final

    # métodos privados
    def __metodo_privado(self):
        print(f'método privado, y la edad es: {self.__edad}')

    def utilizando_privado(self):
        self.__metodo_privado()



"""
carlos = EmployeeEmpty()
print(carlos.name, carlos.last, carlos.salary)

andres = EmployeeEmpty()
print(andres.name, andres.last, andres.salary)
andres.name = 'Andres'
print(andres.name, andres.last, andres.salary)
print(carlos.name, carlos.last, carlos.salary)
print()
"""

julian = Employee('Julian', 'Bermudez', 2000)
print(julian.name, julian.last, julian.salary)

sara = Employee('Sara', 'Corrales', 1000)
print(sara.name, sara.last, sara.salary)

manuela = Employee()
print(manuela.name, manuela.last, manuela.email, manuela.salary)
print()

sara.saludo('Señorita') # Employee.saludo(sara, 'Señorita')
Employee.saludo(sara, 'Señora')
print()

sara.despedida()
Employee.despedida(julian)
print()

sara.despedida_generica()
Employee.despedida_generica()
print()

print('Raise amount:', julian.raise_amount, sara.raise_amount, manuela.raise_amount)
julian.new_raise(2)
print('New Raise amount:', julian.raise_amount, sara.raise_amount, manuela.raise_amount)
print()


print(sara)
print(sara.__repr__())
print()


# julian.__metodo_privado() # -> no me funciona
# print(julian.__edad) # no me funciona
# julian.utilizando_privado()
julian._Employee__metodo_privado()