class Empleados:
    tope = 20000
    # Constructor: se ejecuta en la instanciación de la clase
    def __init__(self, nombre='Empleado', apellido='Compania', salario=10000, edad=30):
        # Atributos vinculados con la instancia
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario
        self.email = self.nombre + '.' + self.apellido + '@loquesea.com'
        # Atributos privados
        self.__edad = edad
        print(self.nombre, self.__edad)

    # método regular: si hace algo con los atributos de la clase
    def cargo(self):
        if self.salario > self.tope:
            return 'TI'
        else:
            return 'RRHH'

    # método estático: no utiliza nada de la clase
    @staticmethod # Decoradores
    def saludo(nombre):
        return f'Hola {nombre}'
    
    # método de clase: este método afectará a la clase y las instancias que hayan
    @classmethod # Decoradores
    def cambio_tope(cls, nuevo_tope):
        cls.tope = nuevo_tope

    # métodos especiales:
    def __str__(self): # Utilizado para presentar la clase al usuario final
        return f'Objeto Empleado: {self.nombre}, {self.apellido}, {self.salario}'
    
    def __repr__(self): # Utilizado para hacer debug
        return f'{self.nombre}, {self.apellido}, {self.salario}'
    
    # métodos privados
    def __alias(self):
        return self.nombre[0] + self.apellido
    
    def print_alias(self):
        return self.__alias()


# Instanciar -> Empleados(gabriel)
gabriel = Empleados('Gabriel', 'Moreno', 20000) # -> Empleados(gabriel, 'Gabriel', 'Moreno', 20000)
camilo = Empleados('Camilo', 'Gomez', 25000, 25)


print(f'nombre de gabriel: {gabriel.nombre}, salario: {gabriel.salario}')
print(f'email de gabriel: {gabriel.email}')
print(f'cargo de gabriel: {gabriel.cargo()}') # Empleados.cargo(gabriel)
# print(Empleados.cargo(gabriel))
print(f'tope: {gabriel.tope}')
print()
print(f'nombre de camilo: {camilo.nombre}, salario: {camilo.salario}')
print(f'email de camilo: {camilo.email}')
print(f'cargo de camilo: {camilo.cargo()}') # Empleados.cargo(camilo)
# print(Empleados.cargo(camilo))
print(f'tope: {camilo.tope}')
print()
print(camilo.saludo('Andres')) # -> Empleados.saludo(camilo)
print(gabriel.saludo('Oscar'))
print()
print(Empleados.tope)
print(f'tope Camilo  antes de: {camilo.tope}')
print(f'tope Gabriel antes de: {gabriel.tope}')
print()
camilo.tope = 21000 # solo afecto a la instancia Camilo
print(Empleados.tope)
print(f'tope Camilo  antes de: {camilo.tope}')
print(f'tope Gabriel antes de: {gabriel.tope}')
print()
camilo.cambio_tope(21000)
print(Empleados.tope)
print(f'tope Camilo despues de: {camilo.tope}')
print(f'tope Gabriel despues de: {gabriel.tope}')
print()
print(camilo)
print(gabriel)
print()
print(camilo.__repr__())
print()
#print(Empleados.__dict__)
#print(camilo._Empleados__edad) # _NombreClase__atributo
#print(camilo._Empleados__alias()) # _NombreClase__funcion
#print(camilo.__dict__)
print(gabriel.print_alias())